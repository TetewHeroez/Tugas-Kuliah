/* ---------------- utilities ---------------- */
const NEG_INF = -1e9; // sentinel for -inf (integer)
function matToKaTeX(m) {
  // Always output n x n matrix, even if input is flat or malformed
  if (!Array.isArray(m)) return "";
  let n = m.length;
  // If m is a flat array, reshape to n x n (try to guess n)
  if (n > 0 && !Array.isArray(m[0])) {
    // Try to guess n as sqrt(length)
    const N = Math.sqrt(m.length) | 0;
    if (N * N === m.length) {
      m = Array.from({ length: N }, (_, i) => m.slice(i * N, (i + 1) * N));
      n = N;
    } else {
      // fallback: treat as 1 row, but pad to square
      n = Math.ceil(Math.sqrt(m.length));
      let arr = m.slice();
      while (arr.length < n * n) arr.push(NEG_INF);
      m = Array.from({ length: n }, (_, i) => arr.slice(i * n, (i + 1) * n));
    }
  }
  // If m is jagged or not n x n, pad/crop rows
  m = m.slice(0, n).map((row) => {
    if (!Array.isArray(row)) row = [row];
    if (row.length < n) return row.concat(Array(n - row.length).fill(NEG_INF));
    return row.slice(0, n);
  });
  // Debug: show matrix as JSON in console
  if (typeof window !== "undefined" && window.DEBUG_MAT) {
    console.log("matToKaTeX rendering:", JSON.stringify(m));
  }
  // Build KaTeX bmatrix string
  // KaTeX needs \\ for new row, but in JS string it must be \\\\ (4x)
  return (
    "\\displaystyle \\begin{bmatrix}" +
    m
      .map((row) =>
        row.map((v) => (v <= NEG_INF / 2 ? "-\\infty" : String(v))).join(" & ")
      )
      .join(" \\\\ ") +
    "\\end{bmatrix}"
  );
}
function randInt(rng, lo, hi) {
  return Math.floor(rng() * (hi - lo + 1)) + lo;
}
function rngFactory(seed) {
  if (seed == null) return () => Math.random();
  let x = seed | 0;
  return () => {
    x ^= x << 13;
    x ^= x >>> 17;
    x ^= x << 5;
    return (x >>> 0) / 4294967295;
  };
}
function bytesToHex(arr) {
  return Array.from(arr)
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

/* --------------- max-plus ops (int) --------------- */
function tropicalMatMul(A, B) {
  const n = A.length,
    p = B[0].length;
  const C = Array.from({ length: n }, () => Array(p).fill(NEG_INF));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < p; j++) {
      let best = NEG_INF;
      for (let k = 0; k < A[0].length; k++) {
        const v = A[i][k] + B[k][j];
        if (v > best) best = v;
      }
      C[i][j] = best;
    }
  }
  return C;
}
function tropicalAdd(A, B) {
  const n = A.length,
    m = A[0].length;
  const C = Array.from({ length: n }, () => Array(m).fill(0));
  for (let i = 0; i < n; i++)
    for (let j = 0; j < m; j++) C[i][j] = Math.max(A[i][j], B[i][j]);
  return C;
}
function scalarTropicalMul(s, A) {
  return A.map((r) => r.map((v) => v + s));
}

/* --------------- LdP generator --------------- */
function ldlpMatrix(n, r, k, seed) {
  const rng = rngFactory(seed);
  const low = 2 * r,
    high = r;
  const minVal = Math.min(low, high);
  const maxVal = Math.max(low, high);
  const M = Array.from({ length: n }, () => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i === j) {
        M[i][j] = k;
      } else {
        // Random value in [2r, r] for all non-diagonal elements, different for each (i,j)
        M[i][j] = minVal === maxVal ? minVal : randInt(rng, minVal, maxVal);
      }
    }
  }
  return M;
}

/* --------------- serialize matrix -> Uint8Array (int32) --------------- */
function matrixToBytesInt32(mat) {
  const n = mat.length;
  const arr = new Int32Array(n * n);
  let idx = 0;
  for (let i = 0; i < n; i++)
    for (let j = 0; j < n; j++) arr[idx++] = mat[i][j] | 0;
  return new Uint8Array(arr.buffer);
}

/* --------------- Ed25519 sign/verify (TweetNaCl) --------------- */
function signDetached(secretKey, dataUint8) {
  return nacl.sign.detached(dataUint8, secretKey);
}
function verifyDetached(publicKey, sig, dataUint8) {
  return nacl.sign.detached.verify(dataUint8, sig, publicKey);
}

/* --------------- WebCrypto HKDF -> AES-GCM --------------- */
async function deriveAesKeyFromMatrix(mat) {
  const ikm = matrixToBytesInt32(mat);
  const baseKey = await crypto.subtle.importKey(
    "raw",
    ikm.buffer,
    "HKDF",
    false,
    ["deriveKey"]
  );
  const salt = new Uint8Array(16); // demo only: zero salt (use random in real)
  const info = new TextEncoder().encode("ldlp-shared-key-v1");
  const derived = await crypto.subtle.deriveKey(
    {
      name: "HKDF",
      hash: "SHA-256",
      salt: salt.buffer,
      info: info.buffer,
    },
    baseKey,
    { name: "AES-GCM", length: 256 },
    true,
    ["encrypt", "decrypt"]
  );
  return derived;
}
async function aesGcmEncrypt(key, plaintextUint8, aadUint8 = new Uint8Array()) {
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const ct = await crypto.subtle.encrypt(
    { name: "AES-GCM", iv, additionalData: aadUint8 },
    key,
    plaintextUint8
  );
  return { iv: new Uint8Array(iv), ct: new Uint8Array(ct) };
}
async function aesGcmDecrypt(key, iv, ct, aad = new Uint8Array()) {
  const pt = await crypto.subtle.decrypt(
    { name: "AES-GCM", iv, additionalData: aad },
    key,
    ct
  );
  return new Uint8Array(pt);
}

/* ----------------- state ----------------- */
let state = {
  n: 3,
  r: -5,
  kA: 10,
  kB: 12,
  alice: { kp: null, mat: null, pubBytes: null, sig: null },
  bob: { kp: null, mat: null, pubBytes: null, sig: null },
  channel: { aliceSent: null, bobSent: null }, // what was sent on network (can be tampered)
  shared: { alice: null, bob: null },
  aesKey: null, // Alice's AES key
  bobAesKey: null, // Bob's AES key (may differ if MITM)
  lastCipher: null,
  eveMitmActive: false, // Flag untuk mendeteksi MITM attack
};

// Global variables untuk Eve MITM
let eveInterceptedCipher = null;
let eveInterceptedPlain = null;
let eveModifiedPlain = null;
let eveMatA = null; // Eve's MITM matrix (pretend Alice->Bob)
let eveMatB = null; // Eve's MITM matrix (pretend Bob->Alice)

/* ---------------- UI wiring ---------------- */
const outSetup = document.getElementById("outSetup");
const outExchange = document.getElementById("outExchange");
const outCrypto = document.getElementById("outCrypto");
const outEve = document.getElementById("outEve");

document.getElementById("btnGenerate").onclick = () => {
  const btnDerive = document.getElementById("btnDerive");
  const btnEncrypt = document.getElementById("btnEncrypt");
  const btnDecrypt = document.getElementById("btnDecrypt");

  // Reset MITM state
  state.eveMitmActive = false;
  eveInterceptedCipher = null;
  eveInterceptedPlain = null;
  eveModifiedPlain = null;
  eveMatA = null;
  eveMatB = null;
  const n = Number(document.getElementById("n").value);
  const r = Number(document.getElementById("r").value);
  const kA = Number(document.getElementById("kA").value);
  const kB = Number(document.getElementById("kB").value);
  state.n = n;
  state.r = r;
  state.kA = kA;
  state.kB = kB;

  // keypairs
  state.alice.kp = nacl.sign.keyPair();
  state.bob.kp = nacl.sign.keyPair();

  // matrices: use random seed so every click gives different matrix
  const seedA = Date.now() + Math.floor(Math.random() * 1000000);
  const seedB = Date.now() + Math.floor(Math.random() * 1000000) + 12345;
  state.alice.mat = ldlpMatrix(n, r, kA, seedA);
  state.bob.mat = ldlpMatrix(n, r, kB, seedB);

  state.alice.pubBytes = matrixToBytesInt32(state.alice.mat);
  state.bob.pubBytes = matrixToBytesInt32(state.bob.mat);

  outSetup.innerHTML = `Generated.<br>
    Alice public key hex (first 16 bytes): <span class="mono">${bytesToHex(
      state.alice.kp.publicKey
    ).slice(0, 32)}</span><br>
    Bob public key hex (first16): <span class="mono">${bytesToHex(
      state.bob.kp.publicKey
    ).slice(0, 32)}</span><br><br>
    Alice matrix:<br>$$${matToKaTeX(state.alice.mat)}$$<br><br>
    Bob matrix:<br>$$${matToKaTeX(state.bob.mat)}$$`;
  if (window.renderMathInElement) renderMathInElement(outSetup);
  outExchange.textContent = "Not exchanged yet";
  outCrypto.textContent = "No key derived";
  outEve.textContent = "No MITM";
  // Reset signature acceptance state
  state._aliceAccepts = true;
  state._bobAccepts = true;

  // Reset AES keys
  state.aesKey = null;
  state.bobAesKey = null;
  state.lastCipher = null;
};

// Enable crypto buttons
btnDerive.disabled = false;
btnEncrypt.disabled = false;
btnDecrypt.disabled = false;
document.getElementById("btnShow").onclick = () => {
  outSetup.innerHTML = `Alice matrix:<br>$$${matToKaTeX(
    state.alice.mat
  )}$$<br><br>Bob matrix:<br>$$${matToKaTeX(state.bob.mat)}$$`;
  if (window.renderMathInElement) renderMathInElement(outSetup);
};

/* Exchange with signatures (honest) */
document.getElementById("btnExchange").onclick = () => {
  // sign public bytes
  state.alice.sig = signDetached(
    state.alice.kp.secretKey,
    state.alice.pubBytes
  );
  state.bob.sig = signDetached(state.bob.kp.secretKey, state.bob.pubBytes);

  // channel carries signed bytes (honest)
  state.channel.aliceSent = {
    data: state.alice.pubBytes,
    sig: state.alice.sig,
    pubkey: state.alice.kp.publicKey,
  };
  state.channel.bobSent = {
    data: state.bob.pubBytes,
    sig: state.bob.sig,
    pubkey: state.bob.kp.publicKey,
  };

  // receivers verify
  const bobVer = verifyDetached(
    state.channel.aliceSent.pubkey,
    state.channel.aliceSent.sig,
    state.channel.aliceSent.data
  );
  const aliceVer = verifyDetached(
    state.channel.bobSent.pubkey,
    state.channel.bobSent.sig,
    state.channel.bobSent.data
  );

  // Enable crypto buttons
  btnDerive.disabled = false;
  btnEncrypt.disabled = false;
  btnDecrypt.disabled = false;
  outExchange.textContent = `Exchange (signed).\nBob verifies Alice: ${bobVer}\nAlice verifies Bob: ${aliceVer}\n\nAlice sent bytes (first 24 hex): ${bytesToHex(
    state.channel.aliceSent.data.slice(0, 24)
  )}...\nBob sent bytes (first 24 hex): ${bytesToHex(
    state.channel.bobSent.data.slice(0, 24)
  )}...`;
  outEve.textContent = "No MITM (honest exchange).";
};

/* Exchange unsigned (allow Eve to MITM replace) */
document.getElementById("btnExchangeNoSign").onclick = () => {
  state.channel.aliceSent = {
    data: state.alice.pubBytes,
    sig: null,
    pubkey: state.alice.kp.publicKey,
  };
  state.channel.bobSent = {
    data: state.bob.pubBytes,
    sig: null,
    pubkey: state.bob.kp.publicKey,
  };
  // Enable crypto buttons
  btnDerive.disabled = false;
  btnEncrypt.disabled = false;
  btnDecrypt.disabled = false;
  outExchange.textContent = `Exchange (unsigned).\nData on channel (can be tampered by Eve).\nAlice bytes: ${bytesToHex(
    state.channel.aliceSent.data.slice(0, 24)
  )}...\nBob bytes: ${bytesToHex(state.channel.bobSent.data.slice(0, 24))}...`;
  outEve.textContent = "Unsigned exchange: Eve can replace packets.";
  // Reset signature acceptance state for unsigned mode
  state._aliceAccepts = true;
  state._bobAccepts = true;
};

/* Eve intercept & replace (MITM) */
document.getElementById("btnEveIntercept").onclick = () => {
  // Set MITM flag
  state.eveMitmActive = true;

  // Eve crafts her own matrices (randomized)
  const n = state.n;
  // Use random seeds for Eve's matrices
  const seedE1 = Date.now() + Math.floor(Math.random() * 1000000) + 22222;
  const seedE2 = Date.now() + Math.floor(Math.random() * 1000000) + 33333;
  eveMatA = ldlpMatrix(n, state.r, 5, seedE1); // pretend to be Alice -> Bob
  eveMatB = ldlpMatrix(n, state.r, 6, seedE2); // pretend to be Bob -> Alice
  const Eb1 = matrixToBytesInt32(eveMatA);
  const Eb2 = matrixToBytesInt32(eveMatB);

  // Replace channel packets
  state.channel.aliceSent = {
    data: Eb1,
    sig: null,
    pubkey: null,
    note: "Eve replaced Alice->Bob",
  };
  state.channel.bobSent = {
    data: Eb2,
    sig: null,
    pubkey: null,
    note: "Eve replaced Bob->Alice",
  };

  outEve.innerHTML = `Eve replaced packets on channel.<br>Eve-&gt;Bob (pretend Alice) matrix:<br>$$${matToKaTeX(
    eveMatA
  )}$$<br><br>Eve-&gt;Alice (pretend Bob) matrix:<br>$$${matToKaTeX(
    eveMatB
  )}$$<br><br>(If signatures not used, Alice & Bob will compute shared matrix with Eve, not each other.)`;
  if (window.renderMathInElement) renderMathInElement(outEve);
};

/* restore honest (use channel what's originally generated) */
document.getElementById("btnEveRestore").onclick = () => {
  // Reset MITM flag
  state.eveMitmActive = false;

  state.channel.aliceSent = {
    data: state.alice.pubBytes,
    sig: state.alice.sig,
    pubkey: state.alice.kp.publicKey,
  };
  state.channel.bobSent = {
    data: state.bob.pubBytes,
    sig: state.bob.sig,
    pubkey: state.bob.kp.publicKey,
  };
  outEve.textContent =
    "Channel restored to honest signed packets (if signatures present).";
};

/* Compute shared matrices at each side using what they received on channel */
document.getElementById("btnCompute").onclick = () => {
  if (!state.channel.aliceSent || !state.channel.bobSent) {
    alert("Do exchange first");
    return;
  }
  // If signatures present, verify before using (simulate receiver)
  let bobAccepts = true,
    aliceAccepts = true;
  if (state.channel.aliceSent.sig) {
    bobAccepts = verifyDetached(
      state.channel.aliceSent.pubkey,
      state.channel.aliceSent.sig,
      state.channel.aliceSent.data
    );
  }
  if (state.channel.bobSent.sig) {
    aliceAccepts = verifyDetached(
      state.channel.bobSent.pubkey,
      state.channel.bobSent.sig,
      state.channel.bobSent.data
    );
  }
  // Store signature acceptance in state for later crypto checks
  state._aliceAccepts = aliceAccepts;
  state._bobAccepts = bobAccepts;

  // Only block key agreement if signatures are present and either party rejects
  const signedMode = !!(
    state.channel.aliceSent.sig || state.channel.bobSent.sig
  );
  if (signedMode && (!aliceAccepts || !bobAccepts)) {
    outExchange.innerHTML = `Signature verification failed!<br>Alice accepted Bob packet? ${aliceAccepts}<br>Bob accepted Alice packet? ${bobAccepts}<br><br><span style=\"color:#dc2626;font-weight:bold\">Key agreement aborted. Cannot derive shared key.</span>`;
    state.shared.alice = null;
    state.shared.bob = null;
    state.aesKey = null;
    state.lastCipher = null;
    if (window.renderMathInElement) renderMathInElement(outExchange);
    return;
  }

  // parse matrices from received bytes
  function bytesToMat32(u8, n) {
    // Validasi buffer size harus tepat n*n*4 bytes (int32)
    const expectedSize = n * n * 4;
    if (u8.byteLength < expectedSize) {
      console.error(
        `Buffer too small: expected ${expectedSize} bytes, got ${u8.byteLength}`
      );
      // Pad dengan NEG_INF jika buffer terlalu kecil
      const paddedBuffer = new ArrayBuffer(expectedSize);
      const paddedView = new Int32Array(paddedBuffer);
      paddedView.fill(NEG_INF);

      // Copy data yang tersedia
      const sourceView = new Int32Array(
        u8.buffer,
        u8.byteOffset,
        Math.floor(u8.byteLength / 4)
      );
      paddedView.set(sourceView);

      const view = paddedView;
      const arr = [];
      let idx = 0;
      for (let i = 0; i < n; i++) {
        const row = [];
        for (let j = 0; j < n; j++) row.push(view[idx++]);
        arr.push(row);
      }
      return arr;
    }

    // Buffer size normal atau lebih besar
    const view = new Int32Array(u8.buffer, u8.byteOffset, n * n);
    const arr = [];
    let idx = 0;
    for (let i = 0; i < n; i++) {
      const row = [];
      for (let j = 0; j < n; j++) row.push(view[idx++]);
      arr.push(row);
    }
    return arr;
  }

  let A_received = bytesToMat32(state.channel.aliceSent.data, state.n); // what Bob sees as "Alice"
  let B_received = bytesToMat32(state.channel.bobSent.data, state.n); // what Alice sees as "Bob"

  // Each uses their own private matrix and received public matrix (here we use full matrices as "public")
  // In our simple model, Alice uses her own mat and B_received, Bob uses A_received and his own mat
  const K_alice = tropicalMatMul(state.alice.mat, B_received);
  const K_bob = tropicalMatMul(A_received, state.bob.mat);

  state.shared.alice = K_alice;
  state.shared.bob = K_bob;

  const isEqual = JSON.stringify(K_alice) === JSON.stringify(K_bob);
  outExchange.innerHTML = `Compute step:<br> Alice accepted Bob packet? ${aliceAccepts}<br>Bob accepted Alice packet? ${bobAccepts}<br><br>Shared (Alice side):<br>$$${matToKaTeX(
    K_alice
  )}$$<br><br>Shared (Bob side):<br>$$${matToKaTeX(
    K_bob
  )}$$<br><br>Equal? ${isEqual}`;
  if (window.renderMathInElement) renderMathInElement(outExchange);

  // Only disable crypto if signed mode and signature fails
  if (signedMode && (!aliceAccepts || !bobAccepts)) {
    state.aesKey = null;
    state.lastCipher = null;
    btnDerive.disabled = true;
    btnEncrypt.disabled = true;
    btnDecrypt.disabled = true;
  }
};

/* Derive AES key (HKDF) */
document.getElementById("btnDerive").onclick = async () => {
  if (!state.shared.alice) {
    alert("Compute shared matrices first");
    return;
  }
  // Only allow if both accepted signature
  if (!state._aliceAccepts || !state._bobAccepts) {
    outCrypto.textContent = "Cannot derive key: signature verification failed.";
    return;
  }

  // Derive key from Alice's shared matrix (Alice's perspective)
  const keyAlice = await deriveAesKeyFromMatrix(state.shared.alice);
  state.aesKey = keyAlice;

  // Also derive Bob's key for comparison (Bob's perspective)
  const keyBob = await deriveAesKeyFromMatrix(state.shared.bob);

  // Check if keys match (should only match in honest case)
  const aliceKeyBytes = await crypto.subtle.exportKey("raw", keyAlice);
  const bobKeyBytes = await crypto.subtle.exportKey("raw", keyBob);
  const keysMatch =
    bytesToHex(new Uint8Array(aliceKeyBytes)) ===
    bytesToHex(new Uint8Array(bobKeyBytes));

  outCrypto.innerHTML = `Derived AES-GCM key (CryptoKey).<br>
    <span style="color:#666">Alice & Bob keys match? ${keysMatch}</span>`;

  // Store Bob's key separately for decrypt simulation
  state.bobAesKey = keyBob;
};

/* Encrypt and decrypt */
document.getElementById("btnEncrypt").onclick = async () => {
  if (!state.aesKey) {
    alert("Derive key first");
    return;
  }
  if (!state._aliceAccepts || !state._bobAccepts) {
    outCrypto.textContent = "Cannot encrypt: signature verification failed.";
    return;
  }
  const pt = new TextEncoder().encode(document.getElementById("msg").value);
  const aad = new TextEncoder().encode("ldlp-demo-aad");
  const { iv, ct } = await aesGcmEncrypt(state.aesKey, pt, aad);
  state.lastCipher = { iv, ct, aad };
  // MITM Eve interception (unsigned mode only)
  if (
    !state.channel.aliceSent.sig &&
    !state.channel.bobSent.sig &&
    eveMatA &&
    eveMatB
  ) {
    // Eve intercepts and can decrypt with Alice's shared key (Eve knows Alice's matrix from MITM)
    try {
      // Eve computes Alice's shared key: Alice_matrix × Eve_matrixB (what Alice thinks is Bob's matrix)
      const aliceSharedWithEve = tropicalMatMul(state.alice.mat, eveMatB);
      const eveKeyFromAlice = await deriveAesKeyFromMatrix(aliceSharedWithEve);

      // Eve decrypts Alice's message using Alice's compromised shared key
      const ptEve = await aesGcmDecrypt(eveKeyFromAlice, iv, ct, aad);
      eveInterceptedCipher = { iv, ct, aad };
      eveInterceptedPlain = new TextDecoder().decode(ptEve);
      eveModifiedPlain = eveInterceptedPlain;

      // Eve UI: modify or inject message
      outEve.innerHTML = `<span style="color:#dc2626;font-weight:bold">🚨 Eve intercepted and can modify the message!</span><br>
        <strong>Original message from Alice:</strong> "${eveInterceptedPlain}"<br><br>
        
        <strong>Modify existing message:</strong><br>
        <textarea id="eveMsgBox" rows="2" style="width:98%">${eveInterceptedPlain}</textarea><br>
        <button id="eveApplyBtn">Apply modification & send to Bob</button>
        
        <hr style='margin:8px 0'>
        
        <strong>OR inject completely new message:</strong><br>
        <textarea id="eveInjectBox" rows="2" style="width:98%" placeholder="Type a new fake message from Alice..."></textarea><br>
        <button id="eveInjectBtn">Send new message as Alice → Bob</button>
        <br><input type="checkbox" id="demoMode" style="margin:8px 0;"> 
        <label for="demoMode" style="font-size:0.9em;color:#666;">Demo Mode: Allow Eve's message to reach Bob (unrealistic but educational)</label>
        
        <br><br><span style="color:#16a34a">✅ Bob will successfully decrypt modified messages because Eve compromised the shared key!</span>
      `;

      // Langsung akses elemen yang baru dibuat tanpa setTimeout
      const eveMsgBox = document.getElementById("eveMsgBox");
      const eveApplyBtn = document.getElementById("eveApplyBtn");
      const eveInjectBox = document.getElementById("eveInjectBox");
      const eveInjectBtn = document.getElementById("eveInjectBtn");

      // Set event handlers langsung setelah innerHTML
      if (eveApplyBtn) {
        eveApplyBtn.onclick = async function () {
          if (!eveMsgBox) return;
          eveModifiedPlain = eveMsgBox.value;
          // Eve re-encrypts with the SAME key Alice used (this is the key vulnerability!)
          // In MITM, Eve knows Alice's key because she replaced Bob's matrix
          const newPt = new TextEncoder().encode(eveModifiedPlain);
          const newCipher = await aesGcmEncrypt(state.aesKey, newPt, aad);
          // Replace ciphertext for Bob
          state.lastCipher = newCipher;
          outEve.innerHTML += `<br><span style="color:#dc2626;font-weight:bold">✅ Modified message sent to Bob:</span><br>
            <span class='mono' style="background:#ffe6e6;padding:4px;border-radius:4px;">"${eveModifiedPlain}"</span><br>
            <span style="color:#f59e0b;font-size:0.9em;">🚨 Bob will successfully decrypt this modified message!</span>`;
        };
      }

      if (eveInjectBtn) {
        eveInjectBtn.onclick = async function () {
          if (!eveInjectBox) return;
          const injectMsg = eveInjectBox.value;
          if (!injectMsg) return;

          const demoMode = document.getElementById("demoMode").checked;

          if (demoMode) {
            // Demo mode: Use Alice's actual key so Bob can decrypt (shows how MITM can work)
            const injectPt = new TextEncoder().encode(injectMsg);
            const injectCipher = await aesGcmEncrypt(
              state.aesKey,
              injectPt,
              aad
            );
            state.lastCipher = injectCipher;
            outEve.innerHTML += `<br><span style="color:#dc2626;font-weight:bold">🚨 [DEMO MODE] Injected message sent to Bob:</span><br>
              <span class='mono' style="background:#ffe6e6;padding:4px;border-radius:4px;">"${injectMsg}"</span><br>
              <span style="color:#16a34a;font-size:0.9em;">✅ Bob will successfully decrypt this (demo mode only)</span>`;
          } else {
            // Realistic mode: Use Alice's key (the vulnerability in unsigned key exchange)
            const injectPt = new TextEncoder().encode(injectMsg);
            const injectCipher = await aesGcmEncrypt(
              state.aesKey,
              injectPt,
              aad
            );
            state.lastCipher = injectCipher;
            outEve.innerHTML += `<br><span style="color:#dc2626;font-weight:bold">🚨 Injected FAKE message sent to Bob:</span><br>
              <span class='mono' style="background:#ffe6e6;padding:4px;border-radius:4px;">"${injectMsg}"</span><br>
              <span style="color:#999;font-size:0.9em;">Bob thinks this message is from Alice! 😈</span><br>
              <span style="color:#16a34a;font-size:0.85em;">✅ Bob will successfully decrypt this because Eve uses Alice's compromised key!</span>`;
          }
        };
      }

      outCrypto.innerHTML = `Encrypted. iv=${bytesToHex(iv)} ct_len=${
        ct.length
      }<br>
        <span style="color:#f59e0b;font-weight:bold">⚠️ WARNING: MITM ACTIVE!</span><br>
        <span style="color:#666">Eve can intercept and modify messages!</span>`;
    } catch (e) {
      outEve.innerHTML = "Eve failed to intercept or modify the message.";
      outCrypto.textContent = `Encrypted. iv=${bytesToHex(iv)} ct_len=${
        ct.length
      }`;
    }
  } else {
    outCrypto.textContent = `Encrypted. iv=${bytesToHex(iv)} ct_len=${
      ct.length
    }`;

    // Jika MITM active, beri peringatan bahwa encrypt berhasil tapi decrypt akan gagal
    if (state.eveMitmActive && eveMatA && eveMatB) {
      outCrypto.innerHTML =
        outCrypto.textContent +
        `<br><span style="color:#f59e0b;font-weight:bold">⚠️ WARNING:</span> 
        <span style="color:#666">MITM active - Bob's decryption will fail due to key mismatch!</span>`;
    }
  }
};

document.getElementById("btnDecrypt").onclick = async () => {
  if (!state.aesKey || !state.lastCipher) {
    alert("Need key and ciphertext");
    return;
  }
  // If signature verification failed, always show decrypt failed (simulate garbage output)
  if (!state._aliceAccepts || !state._bobAccepts) {
    outCrypto.textContent =
      "[WARNING: Signature verification failed!] Decrypt failed: Plaintext is not valid.";
    return;
  }

  try {
    // Bob uses his own derived key (which may be different from Alice's if MITM)
    const bobKey = state.bobAesKey || state.aesKey;
    const pt = await aesGcmDecrypt(
      bobKey,
      state.lastCipher.iv,
      state.lastCipher.ct,
      state.lastCipher.aad
    );
    outCrypto.textContent =
      "Decrypted plaintext: " + new TextDecoder().decode(pt);
  } catch (e) {
    // Normal error handling - should rarely happen now in unsigned MITM mode
    // Dalam unsigned mode, Bob tidak tahu ada MITM - hanya tahu decrypt gagal
    if (!state.channel.aliceSent.sig && !state.channel.bobSent.sig) {
      // Unsigned mode: Bob tidak tahu ada MITM, hanya tahu ada error
      outCrypto.innerHTML = `<span style="color:#dc2626;font-weight:bold">Decrypt failed!</span><br>
        <span style="color:#666">Authentication tag verification failed.</span><br>
        <span style="color:#999">Possible causes: corrupted data, wrong key, or network interference.</span><br>
        <span style="color:#999">Technical error: ${String(e).substring(
          0,
          60
        )}...</span>`;
    } else {
      // Signed mode: Bob bisa detect MITM karena ada signature verification
      if (state.eveMitmActive && eveMatA && eveMatB) {
        outCrypto.innerHTML = `<span style="color:#dc2626;font-weight:bold">🚨 MITM ATTACK DETECTED!</span><br>
          Decrypt failed: Key mismatch due to Eve's interference.<br>
          <span style="color:#666">Bob's key ≠ Alice's encrypted key (Eve modified the channel)</span><br>
          <span style="color:#999">Technical error: ${String(e).substring(
            0,
            80
          )}...</span>`;
      } else {
        outCrypto.textContent = "Decrypt failed: " + String(e);
      }
    }
  }
};
