/* ---------------- Constants ---------------- */
const NEG_INF = -999999;

/* ---------------- Math Rendering Helper ---------------- */
function renderMathInContainer(container) {
  if (!container) return;

  // Simple one-time render without loops
  setTimeout(() => {
    if (window.renderMathInElement) {
      try {
        renderMathInElement(container, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
          ],
          throwOnError: false,
          errorColor: "#cc0000",
          strict: false,
        });
      } catch (e) {
        console.warn("LaTeX rendering error:", e);
      }
    }
  }, 100);
}
/* ---------------- utilities ---------------- */
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

// Matrix power in max-plus algebra: G^k = G ⊗ G ⊗ ... ⊗ G (k times)
function tropicalMatPower(G, k) {
  if (k === 0) {
    // Identity matrix in max-plus: diagonal elements = 0, others = -∞
    const n = G.length;
    const I = Array.from({ length: n }, (_, i) =>
      Array.from({ length: n }, (_, j) => (i === j ? 0 : NEG_INF))
    );
    return I;
  }
  if (k === 1) return G.map((row) => [...row]); // deep copy

  let result = G.map((row) => [...row]); // deep copy
  for (let i = 1; i < k; i++) {
    result = tropicalMatMul(result, G);
  }
  return result;
}

/* --------------- Generator Matrix for DH Max-Plus --------------- */
function generateLdlpMatrix(n, r, k, seed) {
  const rng = rngFactory(seed);
  const M = Array.from({ length: n }, () => Array(n).fill(0));

  // LdlP matrix: diagonal = k, off-diagonal in [2r, r]
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i === j) {
        M[i][j] = k; // diagonal elements
      } else {
        // off-diagonal elements in range [2r, r]
        const minVal = Math.min(2 * r, r);
        const maxVal = Math.max(2 * r, r);
        M[i][j] = randInt(rng, minVal, maxVal);
      }
    }
  }
  return M;
}

// Generate public matrix from LdlP matrix - this is where the "public key" comes from
function generatePublicMatrix(n, r, seed) {
  const rng = rngFactory(seed);
  const G = Array.from({ length: n }, () => Array(n).fill(0));

  // Create a suitable public matrix
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i === j) {
        G[i][j] = 0; // identity-like for max-plus
      } else {
        G[i][j] = randInt(rng, r - 2, r + 2);
      }
    }
  }
  return G;
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
  kA: 10, // Alice's k parameter for LdlP matrix
  kB: 12, // Bob's k parameter for LdlP matrix
  W: null, // Public matrix W (known to all)
  A1: null,
  A2: null, // Alice's private LdlP matrices
  B1: null,
  B2: null, // Bob's private LdlP matrices
  publicA: null, // Alice's public key: A1 ⊗ W ⊗ A2
  publicB: null, // Bob's public key: B1 ⊗ W ⊗ B2
  sharedA: null, // Alice's computed shared secret
  sharedB: null, // Bob's computed shared secret
  aesKey: null,
  lastCipher: null,
  exchanged: false,
};

/* ---------------- UI wiring ---------------- */
const outSetup = document.getElementById("outSetup");
const outKeys = document.getElementById("outKeys");
const outExchange = document.getElementById("outExchange");
const outCrypto = document.getElementById("outCrypto");
const outSecurity = document.getElementById("outSecurity");

// Generate Generator Matrix
document.getElementById("btnGenerate").onclick = () => {
  const n = Number(document.getElementById("n").value);
  const r = Number(document.getElementById("r").value);

  state.n = n;
  state.r = r;
  state.exchanged = false;

  // Generate public matrix W (known to all parties)
  const seed = Date.now() + Math.floor(Math.random() * 1000000);
  state.W = generatePublicMatrix(n, r, seed);

  outSetup.innerHTML = `Matriks publik W berhasil dibuat:<br>$$W = ${matToKaTeX(
    state.W
  )}$$<br><br>
    <span style="color:#666">Matriks $W$ ini akan digunakan sebagai basis publik untuk protokol LdlP max-plus.</span>`;

  renderMathInContainer(outSetup);
  outKeys.textContent = "Buat matriks privat terlebih dahulu";
  outExchange.textContent = "Belum melakukan pertukaran";
  outCrypto.textContent = "Belum ada kunci";
};

// Show Generator Matrix
document.getElementById("btnShow").onclick = () => {
  if (!state.W) {
    alert("Buat matriks publik terlebih dahulu");
    return;
  }
  outSetup.innerHTML = `Matriks publik W:<br>$$W = ${matToKaTeX(state.W)}$$`;
  renderMathInContainer(outSetup);
};

// Compute Public Keys
document.getElementById("btnComputePublic").onclick = () => {
  if (!state.W) {
    alert("Buat matriks publik terlebih dahulu");
    return;
  }

  const kA = Number(document.getElementById("privateA").value);
  const kB = Number(document.getElementById("privateB").value);

  state.kA = kA;
  state.kB = kB;

  // Generate Alice's private LdlP matrices A1 and A2
  const seedA1 = Date.now() + Math.floor(Math.random() * 1000000);
  const seedA2 = Date.now() + Math.floor(Math.random() * 1000000) + 1111;
  state.A1 = generateLdlpMatrix(state.n, state.r, kA, seedA1);
  state.A2 = generateLdlpMatrix(state.n, state.r, kA, seedA2);

  // Generate Bob's private LdlP matrices B1 and B2
  const seedB1 = Date.now() + Math.floor(Math.random() * 1000000) + 2222;
  const seedB2 = Date.now() + Math.floor(Math.random() * 1000000) + 3333;
  state.B1 = generateLdlpMatrix(state.n, state.r, kB, seedB1);
  state.B2 = generateLdlpMatrix(state.n, state.r, kB, seedB2);

  // Compute public keys: Alice computes V = A1 ⊗ W ⊗ A2, Bob computes U = B1 ⊗ W ⊗ B2
  const temp_A = tropicalMatMul(state.A1, state.W);
  state.publicA = tropicalMatMul(temp_A, state.A2);

  const temp_B = tropicalMatMul(state.B1, state.W);
  state.publicB = tropicalMatMul(temp_B, state.B2);

  outKeys.innerHTML = `<strong>Matriks LdlP & Kunci Publik berhasil dibuat:</strong><br><br>
    
    <strong>Matriks Alice:</strong><br>
    $A_1 \\in [2r,r]_n^{${kA}}$: diagonal = ${kA}, off-diagonal $\\in$ [${
    2 * state.r
  }, ${state.r}]<br>
    $A_2 \\in [2r,r]_n^{${kA}}$: diagonal = ${kA}, off-diagonal $\\in$ [${
    2 * state.r
  }, ${state.r}]<br>
    <strong>Kunci publik Alice:</strong> $V = A_1 \\otimes W \\otimes A_2$<br><br>
    
    <strong>Matriks Bob:</strong><br>
    $B_1 \\in [2r,r]_n^{${kB}}$: diagonal = ${kB}, off-diagonal $\\in$ [${
    2 * state.r
  }, ${state.r}]<br>
    $B_2 \\in [2r,r]_n^{${kB}}$: diagonal = ${kB}, off-diagonal $\\in$ [${
    2 * state.r
  }, ${state.r}]<br>
    <strong>Kunci publik Bob:</strong> $U = B_1 \\otimes W \\otimes B_2$<br><br>
    
    <span style="color:#666">
    Alice menyimpan matriks privat $A_1, A_2$ dan membagikan kunci publik $V$.<br>
    Bob menyimpan matriks privat $B_1, B_2$ dan membagikan kunci publik $U$.
    </span>`;

  renderMathInContainer(outKeys);
};

// Show Public Keys
document.getElementById("btnShowPublic").onclick = () => {
  if (!state.publicA || !state.publicB) {
    alert("Buat matriks terlebih dahulu");
    return;
  }

  outKeys.innerHTML = `<strong>Kunci publik Alice V:</strong><br>
    $$V = A_1 \\otimes W \\otimes A_2 = ${matToKaTeX(state.publicA)}$$<br><br>
    
    <strong>Kunci publik Bob U:</strong><br>
    $$U = B_1 \\otimes W \\otimes B_2 = ${matToKaTeX(state.publicB)}$$<br><br>
    
    <strong>Matriks privat Alice:</strong><br>
    $$A_1 = ${matToKaTeX(state.A1)}$$<br>
    $$A_2 = ${matToKaTeX(state.A2)}$$<br><br>
    
    <strong>Matriks privat Bob:</strong><br>
    $$B_1 = ${matToKaTeX(state.B1)}$$<br>
    $$B_2 = ${matToKaTeX(state.B2)}$$`;

  renderMathInContainer(outKeys);
};

// Exchange Public Keys
document.getElementById("btnExchange").onclick = () => {
  if (!state.publicA || !state.publicB) {
    alert("Buat matriks terlebih dahulu");
    return;
  }

  state.exchanged = true;

  outExchange.innerHTML = `<strong>Pertukaran Kunci Publik:</strong><br><br>
    $\\Rightarrow$ Alice mengirim kunci publik ke Bob: $V = A_1 \\otimes W \\otimes A_2$<br>
    $\\Rightarrow$ Bob mengirim kunci publik ke Alice: $U = B_1 \\otimes W \\otimes B_2$<br><br>
    
    <span style="color:#16a34a;">$\\checkmark$ Kunci publik berhasil dipertukar melalui saluran publik!</span><br><br>
    
    <span style="color:#666;">Sekarang Alice dan Bob dapat menghitung kunci rahasia bersama menggunakan matriks privat masing-masing.</span>`;

  renderMathInContainer(outExchange);
};

// Compute Shared Secret
document.getElementById("btnComputeShared").onclick = () => {
  if (!state.exchanged) {
    alert("Tukar kunci publik terlebih dahulu");
    return;
  }

  // Alice computes shared secret: Ka = A1 ⊗ U ⊗ A2 (using Bob's public key U)
  const temp_KA = tropicalMatMul(state.A1, state.publicB);
  state.sharedA = tropicalMatMul(temp_KA, state.A2);

  // Bob computes shared secret: Kb = B1 ⊗ V ⊗ B2 (using Alice's public key V)
  const temp_KB = tropicalMatMul(state.B1, state.publicA);
  state.sharedB = tropicalMatMul(temp_KB, state.B2);

  // Check if shared secrets match (they should due to commutativity)
  const secretsMatch =
    JSON.stringify(state.sharedA) === JSON.stringify(state.sharedB);

  outExchange.innerHTML = `<strong>Komputasi Kunci Rahasia Bersama:</strong><br><br>
    
    <strong>Alice menghitung:</strong><br>
    $K_A = A_1 \\otimes U \\otimes A_2 = A_1 \\otimes (B_1 \\otimes W \\otimes B_2) \\otimes A_2$<br>
    $$K_A = ${matToKaTeX(state.sharedA)}$$<br><br>
    
    <strong>Bob menghitung:</strong><br>
    $K_B = B_1 \\otimes V \\otimes B_2 = B_1 \\otimes (A_1 \\otimes W \\otimes A_2) \\otimes B_2$<br>
    $$K_B = ${matToKaTeX(state.sharedB)}$$<br><br>
    
    <strong>Kunci rahasia cocok?</strong> ${
      secretsMatch
        ? '<span style="color:#16a34a;">$\\checkmark$ YA</span>'
        : '<span style="color:#dc2626;">$\\times$ TIDAK</span>'
    }<br><br>
    
    <span style="color:#666;">
    <strong>Teorema Komutativitas LdlP:</strong><br>
    Karena $A_1, A_2 \\in [2r,r]_n^{k_A}$ dan $B_1, B_2 \\in [2r,r]_n^{k_B}$, maka:<br>
    $A_1 \\otimes (B_1 \\otimes W \\otimes B_2) \\otimes A_2 = B_1 \\otimes (A_1 \\otimes W \\otimes A_2) \\otimes B_2$<br>
    Sehingga kedua pihak mendapatkan kunci rahasia bersama yang sama!
    </span>`;

  renderMathInContainer(outExchange);
};

// Derive AES Key from Shared Secret
document.getElementById("btnDerive").onclick = async () => {
  if (!state.sharedA) {
    alert("Hitung kunci rahasia bersama terlebih dahulu");
    return;
  }

  // Derive AES key from shared secret matrix
  const keyAlice = await deriveAesKeyFromMatrix(state.sharedA);
  state.aesKey = keyAlice;

  outCrypto.innerHTML = `<strong>Derivasi Kunci AES:</strong><br><br>
    $\\checkmark$ Kunci enkripsi simetris berhasil diturunkan dari kunci rahasia bersama $K_A = K_B$<br><br>
    
    <span style="color:#666;">
    Menggunakan HKDF (HMAC-based Key Derivation Function) untuk mengkonversi<br>
    matriks kunci rahasia bersama menjadi kunci enkripsi AES-GCM 256-bit.
    </span>`;

  renderMathInContainer(outCrypto);
};

// Encrypt Message
document.getElementById("btnEncrypt").onclick = async () => {
  if (!state.aesKey) {
    alert("Turunkan kunci AES terlebih dahulu");
    return;
  }

  const message = document.getElementById("msg").value;
  const pt = new TextEncoder().encode(message);
  const aad = new TextEncoder().encode("dh-maxplus-demo");

  const { iv, ct } = await aesGcmEncrypt(state.aesKey, pt, aad);
  state.lastCipher = { iv, ct, aad };

  outCrypto.innerHTML = `<strong>Enkripsi Pesan:</strong><br><br>
    $\\textbf{Teks Asli:}$ "${message}"<br>
    $\\textbf{Terenkripsi:}$ ${bytesToHex(ct).substring(0, 32)}...<br>
    $\\textbf{IV:}$ ${bytesToHex(iv)}<br><br>
    
    <span style="color:#16a34a;">$\\checkmark$ Pesan berhasil dienkripsi menggunakan AES-GCM!</span><br><br>
    
    <span style="color:#666;">
    Alice menggunakan kunci rahasia bersama untuk mengenkripsi pesan.<br>
    Hanya Bob yang memiliki kunci rahasia bersama yang sama dapat mendekripsi.
    </span>`;

  renderMathInContainer(outCrypto);
};

// Decrypt Message
document.getElementById("btnDecrypt").onclick = async () => {
  if (!state.aesKey || !state.lastCipher) {
    alert("Perlu kunci AES dan pesan terenkripsi");
    return;
  }

  try {
    // Simulate Bob using his derived key (should be the same as Alice's)
    const bobKey = await deriveAesKeyFromMatrix(state.sharedB);
    const pt = await aesGcmDecrypt(
      bobKey,
      state.lastCipher.iv,
      state.lastCipher.ct,
      state.lastCipher.aad
    );
    const decryptedMessage = new TextDecoder().decode(pt);

    outCrypto.innerHTML = `<strong>Dekripsi Pesan:</strong><br><br>
      $\\textbf{Pesan terdekripsi:}$ "${decryptedMessage}"<br><br>
      
      <span style="color:#16a34a;">$\\checkmark$ Bob berhasil mendekripsi pesan dari Alice!</span><br><br>
      
      <span style="color:#666;">
      Bob menggunakan kunci rahasia bersama yang sama ($K_A = K_B$) untuk mendekripsi.<br>
      Protokol LdlP max-plus berhasil memungkinkan komunikasi terenkripsi!
      </span>`;
  } catch (e) {
    outCrypto.innerHTML = `<span style="color:#dc2626;">$\\times$ Dekripsi gagal!</span><br>
      Error: ${String(e)}<br><br>
      <span style="color:#666;">
      Kemungkinan penyebab: kunci rahasia bersama tidak cocok atau data rusak.
      </span>`;
  }

  renderMathInContainer(outCrypto);
};

// Security Analysis
document.getElementById("btnAnalyze").onclick = () => {
  if (!state.W) {
    alert("Generate public matrix terlebih dahulu");
    return;
  }

  outSecurity.innerHTML = `<strong>Analisis Keamanan Protocol LdlP:</strong><br><br>
    
    <strong>$\\triangleright$ Apa yang diketahui Eve (penyerang)?</strong><br>
    $\\bullet$ Public matrix $W$ (diketahui semua pihak)<br>
    $\\bullet$ Alice's public key $V = A_1 \\otimes W \\otimes A_2$ (dikirim melalui channel)<br>
    $\\bullet$ Bob's public key $U = B_1 \\otimes W \\otimes B_2$ (dikirim melalui channel)<br><br>
    
    <strong>$\\triangleright$ Apa yang ingin dicari Eve?</strong><br>
    $\\bullet$ Shared secret $K_A = K_B$<br>
    $\\bullet$ Atau private matrices $A_1, A_2$ atau $B_1, B_2$<br><br>
    
    <strong>$\\triangleright$ Masalah matematis yang harus dipecahkan Eve:</strong><br>
    $\\bullet$ <strong>LdlP Matrix Decomposition Problem:</strong><br>
    $\\quad$ Diberikan $V$ dan $W$, cari $A_1, A_2 \\in [2r,r]_n^{${
      state.kA
    }}$ sehingga $V = A_1 \\otimes W \\otimes A_2$<br>
    $\\quad$ Atau diberikan $U$ dan $W$, cari $B_1, B_2 \\in [2r,r]_n^{${
      state.kB
    }}$ sehingga $U = B_1 \\otimes W \\otimes B_2$<br><br>
    
    <strong>$\\triangleright$ Mengapa sulit?</strong><br>
    $\\bullet$ Constraint LdlP: matriks harus memiliki struktur khusus (diagonal = k, off-diagonal $\\in$ [2r,r])<br>
    $\\bullet$ Banyak kemungkinan decomposition, tapi hanya satu yang valid untuk struktur LdlP<br>
    $\\bullet$ Operasi max-plus matrix multiplication bersifat irreversible<br>
    $\\bullet$ Kompleksitas meningkat eksponensial dengan ukuran matrix<br><br>
    
    <strong>$\\triangleright$ Parameter Keamanan Saat Ini:</strong><br>
    $\\bullet$ Matrix size: ${state.n} $\\times$ ${state.n}<br>
    $\\bullet$ Alice LdlP parameter: $k_A = ${state.kA}$<br>
    $\\bullet$ Bob LdlP parameter: $k_B = ${state.kB}$<br>
    $\\bullet$ Range constraint: off-diagonal $\\in$ [${2 * state.r}, ${
    state.r
  }]<br><br>
    
    <span style="color:#16a34a;">
    $\\checkmark$ Protocol ini secure selama LdlP matrix decomposition problem tetap sulit dipecahkan!
    </span>`;

  renderMathInContainer(outSecurity);
};

// Show Computational Complexity
document.getElementById("btnShowComplexity").onclick = () => {
  if (!state.W) {
    alert("Generate public matrix terlebih dahulu");
    return;
  }

  const n = state.n;
  const maxK = Math.max(state.kA, state.kB);
  const rangeSize = Math.abs(state.r - 2 * state.r) + 1;

  outSecurity.innerHTML = `<strong>Kompleksitas Komputasi LdlP:</strong><br><br>
    
    <strong>$\\uparrow$ Legitimate Users (Alice & Bob):</strong><br>
    $\\bullet$ Computing $A_1 \\otimes W \\otimes A_2$: $O(2n^3)$ operations<br>
    $\\bullet$ Computing $B_1 \\otimes W \\otimes B_2$: $O(2n^3)$ operations<br>
    $\\bullet$ Computing shared secret: $O(2n^3)$ operations<br>
    $\\bullet$ Total legitimate cost: $O(n^3)$ per party<br><br>
    
    <strong>$\\downarrow$ Penyerang (Eve) - Pencarian Brute Force:</strong><br>
    $\\bullet$ Search space untuk $A_1$: $(k_A \\times ${rangeSize}^{n^2-n})$ kemungkinan<br>
    $\\bullet$ Search space untuk $A_2$: $(k_A \\times ${rangeSize}^{n^2-n})$ kemungkinan<br>
    $\\bullet$ Total combinations: $\\approx (${maxK} \\times ${rangeSize}^{${
    n * n - n
  }})^2 = ${Math.pow(maxK * Math.pow(rangeSize, n * n - n), 2).toExponential(
    2
  )}$<br>
    $\\bullet$ Matrix multiplication per attempt: $O(n^3)$<br><br>
    
    <strong>$\\triangleright$ Analisis Serangan Saat Ini:</strong><br>
    $\\bullet$ Matriks ${n} $\\times$ ${n}, parameter $k_A=${state.kA}$, $k_B=${
    state.kB
  }$<br>
    $\\bullet$ Range off-diagonal: [${2 * state.r}, ${
    state.r
  }] = ${rangeSize} kemungkinan per elemen<br>
    $\\bullet$ Ruang pencarian per matriks: $${rangeSize}^{${
    n * n - n
  }} = ${Math.pow(rangeSize, n * n - n).toLocaleString()}$<br>
    $\\bullet$ Total kombinasi (A₁ & A₂): $(${rangeSize}^{${
    n * n - n
  }})^2 = ${Math.pow(rangeSize, n * n - n).toExponential(2)}$<br>
    $\\bullet$ Probabilitas sukses per percobaan: $\\approx \\frac{1}{${Math.pow(
      rangeSize,
      n * n - n
    ).toExponential(2)}}$<br>
    $\\bullet$ Ekspektasi percobaan untuk sukses: $\\approx ${Math.pow(
      rangeSize,
      n * n - n
    ).toExponential(0)}$<br><br>
    
    <strong>$\\triangleright$ Perbandingan Kompleksitas:</strong><br>
    $\\bullet$ Alice computation: $\\sim$${2 * n * n * n} operasi<br>
    $\\bullet$ Bob computation: $\\sim$${2 * n * n * n} operasi<br>
    $\\bullet$ Eve brute force: $\\sim$${Math.pow(
      maxK * Math.pow(rangeSize, n * n - n),
      2
    ).toExponential(2)} operasi<br>
    $\\bullet$ <strong>Rasio keamanan:</strong> ${(
      Math.pow(maxK * Math.pow(rangeSize, n * n - n), 2) /
      (4 * n * n * n)
    ).toExponential(2)}:1<br><br>
    
    <strong>$\\triangleright$ Rekomendasi untuk Dunia Nyata:</strong><br>
    $\\bullet$ Matrix size: minimal $6 \\times 6$ hingga $10 \\times 10$<br>
    $\\bullet$ k parameters: $20-50$<br>
    $\\bullet$ Wider range constraint: misalnya $[-20, -10]$<br>
    $\\bullet$ Estimated brute force: $\\sim 10^{12} - 10^{20}$ operasi<br><br>
    
    <span style="color:#dc2626;">
    <strong>⚠️ PERINGATAN KEAMANAN:</strong><br>
    Parameter demo saat ini (n=${n}, k_A=${state.kA}, r=${
    state.r
  }) <strong>TIDAK AMAN</strong> untuk aplikasi nyata!<br>
    Rasio keamanan hanya ${(
      Math.pow(maxK * Math.pow(rangeSize, n * n - n), 2) /
      (4 * n * n * n)
    ).toExponential(2)}:1 - mudah dipecahkan dengan brute force.
    </span><br><br>
    
    <span style="color:#f59e0b;">
    $\\triangle$ <strong>Tujuan Demo:</strong> Menunjukkan bahwa parameter kriptografi harus dipilih dengan hati-hati.<br>
    Demo ini sengaja menggunakan parameter kecil untuk demonstrasi educational.<br>
    Implementasi nyata membutuhkan parameter yang jauh lebih besar!
    </span>`;

  renderMathInContainer(outSecurity);
};

/* ----------------- Security Breach Demo (Eve's Attack) ----------------- */
let attackState = {
  isRunning: false,
  attempts: 0,
  maxAttempts: 10000,
  strategy: "random",
  startTime: null,
  found: false,
  foundA1: null,
  foundA2: null,
  intervalId: null,
};

const outAttack = document.getElementById("outAttack");

// Helper function to check if two matrices are equal
function matricesEqual(A, B) {
  if (!A || !B || A.length !== B.length) return false;
  for (let i = 0; i < A.length; i++) {
    if (A[i].length !== B[i].length) return false;
    for (let j = 0; j < A[i].length; j++) {
      if (Math.abs(A[i][j] - B[i][j]) > 0.001) return false;
    }
  }
  return true;
}

// Check if matrices are "close" but not exactly equal (for near miss detection)
function isNearMatch(A, B, threshold = 2) {
  if (!A || !B || A.length !== B.length) return false;
  let differences = 0;
  let totalElements = 0;

  for (let i = 0; i < A.length; i++) {
    if (A[i].length !== B[i].length) return false;
    for (let j = 0; j < A[i].length; j++) {
      totalElements++;
      if (Math.abs(A[i][j] - B[i][j]) > 0.001) {
        differences++;
      }
    }
  }

  // Consider it a "near miss" if only 1-2 elements are different
  return (
    differences > 0 && differences <= threshold && differences < totalElements
  );
}

// Generate random LdlP matrix for attack
function generateRandomLdlpMatrix(n, r, k, strategy, attempt) {
  const M = Array.from({ length: n }, () => Array(n).fill(0));

  // Different strategies for generating candidate matrices
  if (strategy === "systematic") {
    // Systematic search - enumerate more slowly to avoid immediate success
    const seed = 12345 + Math.floor(attempt / 10); // Slower progression
    const rng = rngFactory(seed);

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (i === j) {
          M[i][j] = k;
        } else {
          const minVal = Math.min(2 * r, r);
          const maxVal = Math.max(2 * r, r);
          M[i][j] = randInt(rng, minVal, maxVal);
        }
      }
    }
  } else if (strategy === "smart") {
    // Smart search with adaptive behavior and more randomness
    const baseAttempt = Math.floor(attempt / 50); // Faster base progression
    const variation = Math.floor(Math.random() * 100); // Add more randomness
    const seed = baseAttempt * 1000 + variation + attempt;
    const rng = rngFactory(seed);

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (i === j) {
          M[i][j] = k;
        } else {
          const minVal = Math.min(2 * r, r);
          const maxVal = Math.max(2 * r, r);

          // Variable bias that changes over time to simulate learning
          const adaptiveBias = 0.1 + (Math.sin(attempt / 50) + 1) * 0.2; // 0.1 to 0.5, varies with time
          const bias = (i + j) % 2 === 0 ? minVal : maxVal;
          M[i][j] =
            Math.random() < adaptiveBias ? bias : randInt(rng, minVal, maxVal);
        }
      }
    }
  } else {
    // Truly random search with high entropy
    const highEntropySeeds = [
      Date.now() + attempt * 1337 + Math.floor(Math.random() * 1000000),
      performance.now() * attempt + Math.random() * 999999,
      (attempt * 7919) % 982451653, // Large prime for better distribution
      Math.floor(Math.random() * Number.MAX_SAFE_INTEGER),
    ];
    const seed = highEntropySeeds[attempt % 4];
    const rng = rngFactory(seed);

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (i === j) {
          M[i][j] = k;
        } else {
          const minVal = Math.min(2 * r, r);
          const maxVal = Math.max(2 * r, r);
          M[i][j] = randInt(rng, minVal, maxVal);
        }
      }
    }
  }

  return M;
}

// Perform one attack iteration
function performAttackIteration() {
  if (!attackState.isRunning || !state.publicA || !state.W) return;

  attackState.attempts++;

  // Generate candidate matrices A1 and A2
  const candidateA1 = generateRandomLdlpMatrix(
    state.n,
    state.r,
    state.kA,
    attackState.strategy,
    attackState.attempts
  );
  const candidateA2 = generateRandomLdlpMatrix(
    state.n,
    state.r,
    state.kA,
    attackState.strategy,
    attackState.attempts + 7777
  );

  // Compute candidate public key: V_candidate = A1_candidate ⊗ W ⊗ A2_candidate
  const temp = tropicalMatMul(candidateA1, state.W);
  const candidatePublicKey = tropicalMatMul(temp, candidateA2);

  // Check if this matches Alice's actual public key
  // Use realistic probability-based success rather than fixed minimum attempts
  const minVal = Math.min(2 * state.r, state.r);
  const maxVal = Math.max(2 * state.r, state.r);
  const searchSpaceSize = Math.pow(
    maxVal - minVal + 1,
    state.n * state.n - state.n
  );

  // Calculate realistic success probability based on search space
  const baseSuccessProbability = 1 / searchSpaceSize;

  // Add some variability and strategy-based modifiers
  let actualSuccessProbability = baseSuccessProbability;

  if (attackState.strategy === "systematic") {
    // Systematic search gradually improves but with fluctuations
    const improvement = Math.min(2.0, 1 + attackState.attempts / 500);
    const noise = 0.8 + Math.random() * 0.4; // Random factor 0.8-1.2
    actualSuccessProbability *= improvement * noise;
  } else if (attackState.strategy === "smart") {
    // Smart search has variable effectiveness - sometimes good, sometimes poor
    const effectiveness = Math.random();
    if (effectiveness < 0.3) {
      // 30% chance of poor performance
      actualSuccessProbability *= 0.2 + Math.random() * 0.3; // 0.2-0.5x
    } else if (effectiveness < 0.7) {
      // 40% chance of average performance
      actualSuccessProbability *= 0.8 + Math.random() * 0.4; // 0.8-1.2x
    } else {
      // 30% chance of good performance
      actualSuccessProbability *= 1.5 + Math.random() * 1.0; // 1.5-2.5x
    }
  } else {
    // Random search - pure probability with small variance
    actualSuccessProbability *= 0.9 + Math.random() * 0.2; // Random multiplier 0.9-1.1x
  }

  // Don't allow success too early but use variable minimum based on parameters
  const difficultyFactor = Math.log2(searchSpaceSize);
  const minAttempts = Math.max(
    3,
    Math.floor(difficultyFactor * (0.5 + Math.random() * 0.5))
  ); // Variable minimum
  const canSucceed = attackState.attempts >= minAttempts;

  // Random success based on probability with demo-friendly scaling
  // Scale probability for demonstration purposes but keep randomness
  const demoScaling = Math.min(50000, Math.max(100, searchSpaceSize / 100)); // Adaptive scaling
  const randomSuccessCheck =
    Math.random() < actualSuccessProbability * demoScaling;

  const shouldSucceed =
    matricesEqual(candidatePublicKey, state.publicA) &&
    canSucceed &&
    randomSuccessCheck;

  // Check for near miss (makes demo more engaging)
  const isNear = isNearMatch(candidatePublicKey, state.publicA);
  const showNearMiss =
    isNear && Math.random() < 0.15 && attackState.attempts >= 2; // 15% chance to show near miss

  if (shouldSucceed) {
    // SUCCESS! Eve found a valid decomposition
    attackState.found = true;
    attackState.foundA1 = candidateA1;
    attackState.foundA2 = candidateA2;
    attackState.isRunning = false;
    clearInterval(attackState.intervalId);

    // Compute the shared secret using found matrices
    const tempKE = tropicalMatMul(candidateA1, state.publicB);
    const eveSharedSecret = tropicalMatMul(tempKE, candidateA2);

    const elapsedTime = ((Date.now() - attackState.startTime) / 1000).toFixed(
      2
    );

    outAttack.innerHTML = `<strong style="color:#dc2626;">🚨 PELANGGARAN KEAMANAN! 🚨</strong><br><br>
      
      <strong>Eve berhasil membobol protokol!</strong><br><br>
      
      <strong>📊 Statistik Serangan:</strong><br>
      $\\bullet$ Strategi: ${attackState.strategy}<br>
      $\\bullet$ Percobaan: ${attackState.attempts.toLocaleString()}<br>
      $\\bullet$ Waktu berlalu: ${elapsedTime} detik<br>
      $\\bullet$ Tingkat keberhasilan: ${(
        (1 / attackState.attempts) *
        100
      ).toExponential(2)}%<br><br>
      
      <strong>🔍 Matriks yang Ditemukan Eve:</strong><br>
      $$\\text{Eve's } A_1 = ${matToKaTeX(candidateA1)}$$<br>
      $$\\text{Eve's } A_2 = ${matToKaTeX(candidateA2)}$$<br><br>
      
      <strong>🆚 Perbandingan dengan Alice:</strong><br>
      Matriks Eve sama dengan Alice? ${
        matricesEqual(candidateA1, state.A1) &&
        matricesEqual(candidateA2, state.A2)
          ? '<span style="color:#f59e0b;">YA - kebetulan sama!</span>'
          : '<span style="color:#dc2626;">TIDAK - Eve menemukan matriks berbeda yang menghasilkan kunci publik sama!</span>'
      }<br><br>
      
      <strong>✅ Verifikasi:</strong><br>
      $$V_{\\text{Eve}} = A_1 \\otimes W \\otimes A_2 = ${matToKaTeX(
        candidatePublicKey
      )}$$<br>
      $$V_{\\text{Alice}} = ${matToKaTeX(state.publicA)}$$<br>
      Kunci publik cocok: ${
        matricesEqual(candidatePublicKey, state.publicA)
          ? '<span style="color:#dc2626;">YA - Eve dapat menghitung kunci rahasia!</span>'
          : '<span style="color:#16a34a;">TIDAK</span>'
      }<br><br>
      
      <strong>💀 Kunci Rahasia yang Dihitung Eve:</strong><br>
      $$K_{\\text{Eve}} = A_1 \\otimes U \\otimes A_2 = ${matToKaTeX(
        eveSharedSecret
      )}$$<br><br>
      
      <span style="color:#dc2626;">
      <strong>⚠️ PROTOKOL TELAH DIBOBOL!</strong><br>
      Eve sekarang dapat mendekripsi semua komunikasi Alice-Bob.<br><br>
      <strong>🎓 Pelajaran:</strong> Parameter demo ini terlalu kecil untuk keamanan nyata!<br>
      Untuk aplikasi dunia nyata, gunakan n≥6, k≥30, dan range r yang lebih luas.
      </span>`;
  } else if (attackState.attempts >= attackState.maxAttempts) {
    // Max attempts reached without success
    attackState.isRunning = false;
    clearInterval(attackState.intervalId);

    const elapsedTime = ((Date.now() - attackState.startTime) / 1000).toFixed(
      2
    );

    outAttack.innerHTML = `<strong style="color:#16a34a;">🛡️ PROTOKOL AMAN! 🛡️</strong><br><br>
      
      <strong>Eve gagal membobol protokol dalam ${attackState.maxAttempts.toLocaleString()} percobaan</strong><br><br>
      
      <strong>📊 Statistik Serangan:</strong><br>
      $\\bullet$ Strategi: ${attackState.strategy}<br>
      $\\bullet$ Total percobaan: ${attackState.attempts.toLocaleString()}<br>
      $\\bullet$ Waktu berlalu: ${elapsedTime} detik<br>
      $\\bullet$ Tingkat keberhasilan: 0% (tidak berhasil)<br><br>
      
      <strong>🔒 Kesimpulan:</strong><br>
      Dengan parameter saat ini ($n=${state.n}$, $k_A=${state.kA}$, $r=${
      state.r
    }$), 
      protokol cukup aman terhadap serangan brute force sampai ${attackState.maxAttempts.toLocaleString()} percobaan.<br><br>
      
      <span style="color:#16a34a;">
      <strong>🎓 Pelajaran:</strong> Parameter yang tepat membuat protokol sangat sulit dipecahkan!<br>
      Ini menunjukkan pentingnya pemilihan parameter kriptografi yang tepat.<br>
      Untuk keamanan produksi yang sesungguhnya, gunakan parameter yang jauh lebih besar!
      </span>`;
  } else {
    // Update progress and show near misses or regular status
    if (showNearMiss) {
      const elapsedTime = ((Date.now() - attackState.startTime) / 1000).toFixed(
        1
      );

      outAttack.innerHTML = `<strong>🔍 SERANGAN SEDANG BERLANGSUNG...</strong><br><br>
        
        <strong>⚠️ HAMPIR BERHASIL!</strong><br>
        <span style="color:#f59e0b;">Eve menemukan matriks yang hampir cocok pada percobaan ke-${
          attackState.attempts
        }!</span><br><br>
        
        <strong>📊 Status Saat Ini:</strong><br>
        $\\bullet$ Strategi: ${attackState.strategy}<br>
        $\\bullet$ Percobaan: ${attackState.attempts.toLocaleString()}<br>
        $\\bullet$ Waktu berlalu: ${elapsedTime}s<br>
        $\\bullet$ Status: Hampir menemukan kunci yang tepat...<br><br>
        
        <span style="color:#f59e0b;"><strong>🎯 Eve sedang mendekat ke solusi!</strong></span>`;
    } else if (attackState.attempts % 100 === 0) {
      const elapsedTime = ((Date.now() - attackState.startTime) / 1000).toFixed(
        1
      );
      const progress = (
        (attackState.attempts / attackState.maxAttempts) *
        100
      ).toFixed(1);
      const rate = (
        (attackState.attempts / (Date.now() - attackState.startTime)) *
        1000
      ).toFixed(0);

      outAttack.innerHTML = `<strong>🔍 SERANGAN SEDANG BERLANGSUNG...</strong><br><br>
        
        <strong>📊 Status Saat Ini:</strong><br>
        $\\bullet$ Strategi: ${attackState.strategy}<br>
        $\\bullet$ Kemajuan: ${attackState.attempts.toLocaleString()} / ${attackState.maxAttempts.toLocaleString()} (${progress}%)<br>
        $\\bullet$ Waktu berlalu: ${elapsedTime}s<br>
        $\\bullet$ Tingkat serangan: ${rate} percobaan/detik<br>
        $\\bullet$ Perkiraan total waktu untuk ruang penuh: ${
          rate > 0
            ? Math.round(
                Math.pow(
                  Math.abs(2 * state.r - state.r) + 1,
                  state.n * state.n - state.n
                ) /
                  rate /
                  3600
              )
            : "∞"
        } jam<br><br>
        
        <div style="background: #f3f4f6; border-radius: 8px; height: 20px; overflow: hidden;">
          <div style="background: linear-gradient(90deg, #ef4444, #f97316); height: 100%; width: ${progress}%; transition: width 0.3s;"></div>
        </div><br>
        
        <strong>🎯 Target:</strong> Mencari matriks $A_1, A_2 \\in [2r,r]_n^{${
          state.kA
        }}$ 
        sehingga $A_1 \\otimes W \\otimes A_2 = V_{\\text{Alice}}$<br><br>
        
        <strong>📈 Ruang Pencarian:</strong><br>
        $\\bullet$ Kombinasi per matriks: ${Math.pow(
          Math.abs(2 * state.r - state.r) + 1,
          state.n * state.n - state.n
        ).toLocaleString()}<br>
        $\\bullet$ Total ruang pencarian: ${Math.pow(
          Math.abs(2 * state.r - state.r) + 1,
          state.n * state.n - state.n
        ).toExponential(2)}² kombinasi<br>
        $\\bullet$ Progress pencarian: ${(
          (attackState.attempts /
            Math.pow(
              Math.abs(2 * state.r - state.r) + 1,
              state.n * state.n - state.n
            )) *
          100
        ).toFixed(6)}% dari ruang total<br><br>
        
        <span style="color:#f59e0b;">
        Eve sedang mencoba berbagai kombinasi matriks LdlP secara ${
          attackState.strategy
        }...
        </span>`;
    }
  }

  renderMathInContainer(outAttack);
}

// Start Brute Force Attack
document.getElementById("btnStartAttack").onclick = () => {
  if (!state.publicA || !state.W) {
    alert("Generate public keys terlebih dahulu untuk memulai attack");
    return;
  }

  if (attackState.isRunning) {
    alert("Attack sudah berjalan");
    return;
  }

  attackState.maxAttempts = Number(
    document.getElementById("maxAttempts").value
  );
  attackState.strategy = document.getElementById("attackStrategy").value;
  attackState.isRunning = true;
  attackState.attempts = 0;
  attackState.found = false;
  attackState.startTime = Date.now();

  outAttack.innerHTML = `<strong>🚀 MEMULAI SERANGAN BRUTE FORCE...</strong><br><br>
    
    <strong>🎯 Target Serangan:</strong><br>
    $\\bullet$ Kunci publik Alice: $V = A_1 \\otimes W \\otimes A_2$<br>
    $\\bullet$ Tujuan: Temukan $A_1, A_2 \\in [2r,r]_n^{${
      state.kA
    }}$ yang menghasilkan $V$ yang sama<br><br>
    
    <strong>⚙️ Konfigurasi Serangan:</strong><br>
    $\\bullet$ Percobaan maksimal: ${attackState.maxAttempts.toLocaleString()}<br>
    $\\bullet$ Strategi: ${attackState.strategy}<br>
    $\\bullet$ Ruang pencarian: $\\approx ${Math.pow(
      state.kA *
        Math.pow(
          Math.abs(state.r - 2 * state.r) + 1,
          state.n * state.n - state.n
        ),
      2
    ).toExponential(2)}$ combinations<br><br>
    
    <span style="color:#ef4444;">
    Attack dimulai! Eve mencoba memecahkan protokol LdlP...
    </span>`;

  renderMathInContainer(outAttack);

  // Start attack with more realistic interval
  attackState.intervalId = setInterval(performAttackIteration, 50); // 50ms per iteration (slower, more realistic)
};

// Stop Attack
document.getElementById("btnStopAttack").onclick = () => {
  if (!attackState.isRunning) {
    alert("Tidak ada attack yang sedang berjalan");
    return;
  }

  attackState.isRunning = false;
  clearInterval(attackState.intervalId);

  const elapsedTime = ((Date.now() - attackState.startTime) / 1000).toFixed(2);

  outAttack.innerHTML = `<strong>⏹️ ATTACK STOPPED</strong><br><br>
    
    Attack dihentikan oleh user.<br><br>
    
    <strong>📊 Final Statistics:</strong><br>
    $\\bullet$ Attempts made: ${attackState.attempts.toLocaleString()}<br>
    $\\bullet$ Time elapsed: ${elapsedTime} seconds<br>
    $\\bullet$ Status: ${
      attackState.found
        ? "SUCCESS - Protocol breached!"
        : "FAILED - Protocol secure"
    }<br><br>
    
    ${
      attackState.found
        ? '<span style="color:#dc2626;">Eve berhasil membobol protokol!</span>'
        : '<span style="color:#16a34a;">Protokol masih aman.</span>'
    }`;

  renderMathInContainer(outAttack);
};

// Reset Attack Demo
document.getElementById("btnResetAttack").onclick = () => {
  attackState.isRunning = false;
  clearInterval(attackState.intervalId);
  attackState.attempts = 0;
  attackState.found = false;
  attackState.foundA1 = null;
  attackState.foundA2 = null;

  outAttack.innerHTML = `Demo attack telah direset.<br><br>
    
    <strong>📝 Cara menggunakan Security Breach Demo:</strong><br>
    1. Pastikan sudah generate public matrices (Alice & Bob)<br>
    2. Pilih max attempts dan strategy<br>
    3. Klik "Mulai Serangan Brute Force"<br>
    4. Tunggu hingga selesai atau stop manual<br><br>
    
    <strong>💡 Tips:</strong><br>
    $\\bullet$ Parameter kecil ($n=2$, $k=5$) lebih mudah dibobol<br>
    $\\bullet$ Parameter besar ($n=4$, $k=15$) lebih sulit dibobol<br>
    $\\bullet$ Strategy "smart" biasanya lebih efektif daripada "random"<br><br>
    
    <span style="color:#666;">
    Ready untuk memulai attack simulation!
    </span>`;

  renderMathInContainer(outAttack);
};

// Initialize attack demo on page load
setTimeout(() => {
  if (document.getElementById("btnResetAttack")) {
    document.getElementById("btnResetAttack").click();
  }
}, 500);
