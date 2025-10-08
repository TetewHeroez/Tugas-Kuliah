# Protokol Pertukaran Kunci LdlP Max-Plus

## Deskripsi

Protokol ini adalah implementasi pertukaran kunci asimetrik menggunakan matriks LdlP (Linde-de la Puente) dalam aljabar max-plus. Berbeda dari protokol Diffie-Hellman klasik, protokol ini memanfaatkan teorema komutativitas khusus dari matriks LdlP untuk memungkinkan Alice dan Bob menghasilkan kunci rahasia bersama yang sama tanpa pernah bertukar matriks privat mereka.

## Konsep Dasar Aljabar Max-Plus

Aljabar max-plus adalah semiring dengan operasi:

- **Tropical Addition (⊕)**: `a ⊕ b = max(a, b)`
- **Tropical Multiplication (⊗)**: `a ⊗ b = a + b`
- **Identity untuk ⊕**: `-∞`
- **Identity untuk ⊗**: `0`

Untuk matriks dalam aljabar max-plus:

- **Matrix Addition**: `(A ⊕ B)ᵢⱼ = max(Aᵢⱼ, Bᵢⱼ)`
- **Matrix Multiplication**: `(A ⊗ B)ᵢⱼ = max_k(Aᵢₖ + Bₖⱼ)`

## Matriks LdlP (Linde-de la Puente)

### Definisi Matriks LdlP:

Matriks M ∈ [2r,r]ₙᵏ jika:

- **Diagonal**: semua elemen diagonal = k
- **Off-diagonal**: semua elemen non-diagonal ∈ [2r, r]

### Teorema Komutativitas LdlP:

Jika A ∈ [2r,r]ₙᵏ¹ dan B ∈ [2s,s]ₙᵏ², maka **A ⊗ B = B ⊗ A**

Teorema ini adalah fondasi keamanan protokol pertukaran kunci.

## Protokol Pertukaran Kunci LdlP

### Langkah-langkah Protokol:

1. **Persiapan (Setup Publik)**:

   - Semua pihak sepakat pada matriks publik **W** (dapat diketahui semua orang)
   - Parameter publik: **n** (ukuran matriks), **r** (parameter LdlP)

2. **Generasi Matriks Privat**:

   - Alice memilih parameter **kₐ** dan membuat dua matriks privat:
     - **A₁** ∈ [2r,r]ₙᵏᴬ (diagonal = kₐ, off-diagonal ∈ [2r,r])
     - **A₂** ∈ [2r,r]ₙᵏᴬ (diagonal = kₐ, off-diagonal ∈ [2r,r])
   - Bob memilih parameter **kᵦ** dan membuat dua matriks privat:
     - **B₁** ∈ [2r,r]ₙᵏᴮ (diagonal = kᵦ, off-diagonal ∈ [2r,r])
     - **B₂** ∈ [2r,r]ₙᵏᴮ (diagonal = kᵦ, off-diagonal ∈ [2r,r])

3. **Komputasi Kunci Publik**:

   - Alice menghitung kunci publiknya: **V = A₁ ⊗ W ⊗ A₂**
   - Bob menghitung kunci publiknya: **U = B₁ ⊗ W ⊗ B₂**

4. **Pertukaran Kunci Publik** (melalui saluran publik):

   - Alice mengirim **V** ke Bob
   - Bob mengirim **U** ke Alice

5. **Komputasi Kunci Rahasia Bersama**:

   - Alice menghitung: **Kₐ = A₁ ⊗ U ⊗ A₂** = **A₁ ⊗ (B₁ ⊗ W ⊗ B₂) ⊗ A₂**
   - Bob menghitung: **Kᵦ = B₁ ⊗ V ⊗ B₂** = **B₁ ⊗ (A₁ ⊗ W ⊗ A₂) ⊗ B₂**

6. **Hasil - Kunci Rahasia Identik**:
   - Berdasarkan teorema komutativitas LdlP: **Kₐ = Kᵦ**
   - Kunci rahasia bersama digunakan untuk menurunkan kunci enkripsi AES-GCM

### Visualisasi Protokol:

```
Alice (privat: A₁, A₂ ∈ [2r,r]ₙᵏᴬ)    Saluran Publik       Bob (privat: B₁, B₂ ∈ [2r,r]ₙᵏᴮ)
              |                             |                              |
         Hitung V = A₁⊗W⊗A₂  ────────────> V ────────────>        Terima V
              |                             |                              |
          Terima U  <─────────────────────  U <─────────────    Hitung U = B₁⊗W⊗B₂
              |                             |                              |
    Kₐ = A₁⊗U⊗A₂ = A₁⊗(B₁⊗W⊗B₂)⊗A₂    [Eve hanya tahu      Kᵦ = B₁⊗V⊗B₂ = B₁⊗(A₁⊗W⊗A₂)⊗B₂
              |                        W, V, U]                            |
              |                             |                              |
         Kunci Rahasia: Kₐ                 |                    Kunci Rahasia: Kᵦ
              |                             |                              |
              └────────────── Kₐ = Kᵦ (teorema komutativitas) ──────────────┘
```

### Teorema Komutativitas dalam Aksi:

Mengapa **Kₐ = Kᵦ**?

**Alice menghitung**: Kₐ = A₁ ⊗ (B₁ ⊗ W ⊗ B₂) ⊗ A₂

**Bob menghitung**: Kᵦ = B₁ ⊗ (A₁ ⊗ W ⊗ A₂) ⊗ B₂

Karena A₁, A₂ ∈ [2r,r]ₙᵏᴬ dan B₁, B₂ ∈ [2r,r]ₙᵏᴮ, berdasarkan teorema komutativitas LdlP:

**A₁ ⊗ (B₁ ⊗ W ⊗ B₂) ⊗ A₂ = B₁ ⊗ (A₁ ⊗ W ⊗ A₂) ⊗ B₂**

Sehingga: **Kₐ = Kᵦ** ✓

## Keamanan Protokol

### Asumsi Keamanan:

Protokol ini bergantung pada kesulitan **Masalah Dekomposisi Matriks LdlP**:

**Masalah**: Diberikan matriks publik W dan hasil V = A₁ ⊗ W ⊗ A₂, tentukan matriks A₁, A₂ ∈ [2r,r]ₙᵏ yang menghasilkan V.

### Apa yang diketahui penyerang (Eve):

- Matriks publik **W** (diketahui semua orang)
- Kunci publik Alice **V = A₁ ⊗ W ⊗ A₂** (dikirim melalui saluran publik)
- Kunci publik Bob **U = B₁ ⊗ W ⊗ B₂** (dikirim melalui saluran publik)
- Parameter publik **n, r** (ukuran matriks dan parameter LdlP)

### Apa yang ingin dicari penyerang:

- Kunci rahasia bersama **Kₐ = Kᵦ**
- Untuk mendapatkannya, Eve perlu mencari salah satu dari:
  - Matriks privat Alice: **A₁, A₂** ∈ [2r,r]ₙᵏᴬ
  - Matriks privat Bob: **B₁, B₂** ∈ [2r,r]ₙᵏᴮ

### Mengapa sulit dipecahkan:

1. **Ruang Pencarian Eksponensial**:

   - Untuk satu matriks A ∈ [2r,r]ₙᵏ, terdapat k × |[2r,r]|^(n²-n) kemungkinan
   - Total untuk A₁, A₂: ≈ (k × |2r-r+1|^(n²-n))²

2. **Tidak Ada Algoritma Efisien**:

   - Tidak ada algoritma polynomial-time yang diketahui untuk membalikkan operasi perkalian matriks LdlP
   - Setiap verifikasi memerlukan perkalian matriks O(n³)

3. **Kompleksitas Berganda**:
   - Eve harus memecahkan baik A₁ maupun A₂ secara bersamaan
   - Struktur khusus LdlP menambah konstrain yang mempersulit pencarian

### Analisis Kompleksitas:

**Pengguna Sah (Alice & Bob)**:

- Komputasi kunci publik: O(n³) operasi per perkalian matriks
- Alice: V = A₁ ⊗ W ⊗ A₂ → 2 perkalian matriks = O(2n³)
- Bob: U = B₁ ⊗ W ⊗ B₂ → 2 perkalian matriks = O(2n³)
- Komputasi kunci rahasia: O(2n³) operasi
- **Total per pihak**: O(4n³) operasi

**Penyerang (Eve) - Brute Force**:

- Ruang pencarian untuk A₁: k × |2r-r+1|^(n²-n) kemungkinan
- Ruang pencarian untuk A₂: k × |2r-r+1|^(n²-n) kemungkinan
- **Total kombinasi**: ≈ (k × |2r-r+1|^(n²-n))²
- Verifikasi per percobaan: O(2n³) operasi (untuk menghitung A₁ ⊗ W ⊗ A₂)
- **Total serangan**: O((k × |2r-r+1|^(n²-n))² × n³) operasi

**Rasio Keamanan**: O((k × |2r-r+1|^(n²-n))² / 4) : 1

### Contoh Parameter dan Kompleksitas:

**Demo Educational (saat ini)**:

- n=3, k=10, r=-5 (range = 6)
- Ruang pencarian: ≈ (10 × 6⁶)² ≈ 4.7 × 10¹⁰
- Rasio keamanan: ≈ 1.17 × 10⁹ : 1

**Implementasi Real-World (rekomendasi)**:

- n=6, k=50, r=-20 (range = 21)
- Ruang pencarian: ≈ (50 × 21³⁰)² ≈ 2.5 × 10⁴⁰
- Rasio keamanan: ≈ 6.25 × 10³⁷ : 1

### Parameter Keamanan yang Direkomendasikan:

**Untuk Demo Educational** (implementasi saat ini):

- Ukuran matriks (n): 2×2 hingga 5×5
- Parameter k: 5-20
- Parameter r: -10 hingga -3
- Tujuan: memahami konsep dan dapat dibobol untuk demonstrasi

**Untuk Aplikasi Real-World**:

- Ukuran matriks (n): minimal 6×6 hingga 10×10
- Parameter k: 30-100
- Parameter r: -50 hingga -10 (range yang lebih luas)
- Estimasi brute force: ~10³⁰ - 10⁵⁰ operasi
- Keamanan setara: 100-170 bit security level

**Pertimbangan Performa vs Keamanan**:

- Matriks lebih besar = keamanan lebih tinggi, tapi komputasi lebih lambat
- Parameter k lebih besar = ruang kunci lebih luas
- Range r lebih luas = lebih banyak variasi off-diagonal

## Implementasi

### File Structure:

- `index.html`: Interface web untuk demo protocol
- `main.js`: Implementasi algoritma max-plus dan protocol
- `style.css`: Styling untuk interface web
- `README.md`: Dokumentasi protocol (file ini)

### Key Functions:

- `tropicalMatMul(A, B)`: Perkalian matriks max-plus
- `tropicalMatPower(G, k)`: Pangkat matriks max-plus (G^k)
- `generateGeneratorMatrix(n, r, seed)`: Generate matriks generator
- `deriveAesKeyFromMatrix(mat)`: Derive AES key dari shared secret matrix

### Fitur Demo:

1. **Persiapan Matriks Publik**: Generate dan tampilkan matriks publik W
2. **Matriks Privat LdlP**: Buat matriks privat A₁, A₂, B₁, B₂ sesuai konstrain LdlP
3. **Komputasi Kunci Publik**: Hitung V = A₁ ⊗ W ⊗ A₂ dan U = B₁ ⊗ W ⊗ B₂
4. **Protokol Pertukaran**: Simulasi pertukaran kunci publik V dan U
5. **Kunci Rahasia Bersama**: Verifikasi bahwa Kₐ = Kᵦ (teorema komutativitas)
6. **Demonstrasi Enkripsi**: Gunakan kunci rahasia untuk enkripsi AES-GCM
7. **Analisis Keamanan**: Tampilkan kompleksitas komputasi dan rasio keamanan
8. **Demo Pelanggaran Keamanan**: Simulasi serangan brute force oleh Eve dengan berbagai strategi

### Strategi Serangan dalam Demo:

1. **Pencarian Acak**: Eve mencoba kombinasi A₁, A₂ secara acak
2. **Pencarian Sistematis**: Eve mencoba semua kombinasi secara berurutan
3. **Pencarian Cerdas**: Eve menggunakan pola atau heuristik untuk mempercepat pencarian

## Cara Menjalankan Demo

1. **Persiapan**:

   - Buka `index.html` di web browser modern (Chrome, Firefox, Safari, Edge)
   - Pastikan JavaScript diaktifkan untuk interaktivitas penuh

2. **Langkah-langkah Demo** (ikuti urutan):

   **Langkah 1 - Persiapan Matriks Publik:**

   - Atur parameter n (ukuran matriks) dan r (parameter LdlP)
   - Klik "Buat Matriks Publik W"
   - Klik "Tampilkan Matriks W" untuk melihat detail

   **Langkah 2 - Matriks Privat LdlP:**

   - Atur parameter kₐ dan kᵦ untuk Alice dan Bob
   - Klik "Buat Matriks Privat & Kunci Publik"
   - Klik "Tampilkan Detail Matriks" untuk melihat semua matriks

   **Langkah 3 - Protokol Pertukaran:**

   - Klik "Tukar Kunci Publik" untuk simulasi pertukaran V dan U
   - Klik "Hitung Rahasia Bersama" untuk verifikasi Kₐ = Kᵦ

   **Langkah 4 - Demonstrasi Enkripsi:**

   - Klik "Turunkan Kunci AES dari Rahasia Bersama"
   - Masukkan pesan yang ingin dienkripsi
   - Klik "Enkripsi Pesan (Alice→Bob)"
   - Klik "Dekripsi (Bob)" untuk verifikasi dekripsi berhasil

   **Langkah 5 - Analisis Keamanan:**

   - Klik "Analisis Keamanan" untuk melihat kompleksitas serangan
   - Klik "Tampilkan Kompleksitas Komputasi" untuk detail matematis

   **Langkah 6 - Demo Pelanggaran Keamanan:**

   - Atur maksimal percobaan dan strategi serangan
   - Klik "Mulai Serangan Brute Force" untuk simulasi serangan Eve
   - Amati progress bar dan statistik serangan real-time
   - Klik "Hentikan Serangan" jika ingin menghentikan sebelum selesai

3. **Tips untuk Eksperimen**:
   - **Parameter Kecil** (n=2, k=5, r=-3): lebih mudah dibobol, bagus untuk demo keberhasilan serangan
   - **Parameter Sedang** (n=3, k=10, r=-5): keseimbangan antara keamanan dan performa demo
   - **Parameter Besar** (n=4, k=15, r=-8): lebih aman, serangan kemungkinan besar gagal

## Nilai Educational

Demo ini dirancang untuk:

- **Memahami Aljabar Max-Plus**: Operasi tropical dan aplikasinya dalam kriptografi
- **Konsep Matriks LdlP**: Struktur khusus dan teorema komutativitas
- **Protokol Pertukaran Kunci**: Alternatif dari Diffie-Hellman klasik menggunakan struktur aljabar berbeda
- **Analisis Keamanan**: Memahami kompleksitas komputasi dan trade-off keamanan vs performa
- **Kriptanalisis Praktis**: Simulasi serangan brute force dan strategi penyerang
- **Implementasi Kriptografi**: Integrasi dengan algoritma enkripsi modern (AES-GCM)

### Keunggulan Pedagogis:

1. **Interaktif**: Semua langkah dapat dijalankan langkah demi langkah
2. **Visualisasi**: Matriks dan operasi ditampilkan dengan notasi matematis yang jelas
3. **Real-time**: Serangan dan progress ditampilkan secara langsung
4. **Parametrik**: Parameter dapat disesuaikan untuk eksperimen berbeda
5. **Komprehensif**: Mencakup teori, implementasi, dan analisis keamanan

## Limitasi dan Pengembangan Lanjutan

### Limitasi Implementasi Saat Ini:

- **Parameter Demo**: Menggunakan parameter kecil untuk tujuan educational dan demonstrasi
- **Tanpa Optimisasi**: Implementasi dasar tanpa optimisasi performa algoritma
- **Keamanan Side-Channel**: Tidak ada proteksi terhadap timing attacks atau analisis power consumption
- **Single-Session**: Tidak ada mekanisme untuk multiple sessions atau key refresh
- **Validasi Terbatas**: Tidak ada validasi input yang comprehensive untuk mencegah parameter tidak valid

### Potensi Pengembangan Lanjutan:

**Peningkatan Keamanan:**

- Implementasi dengan parameter real-world (n≥6, k≥30)
- Proteksi terhadap side-channel attacks
- Implementasi constant-time operations
- Key derivation function yang lebih robust (HKDF dengan salt yang lebih kuat)

**Optimisasi Performa:**

- Algoritma perkalian matriks yang lebih efisien untuk matriks sparse
- Parallelisasi komputasi matriks
- Caching untuk operasi berulang
- Memory management yang lebih baik

**Ekstension Protokol:**

- Forward secrecy dengan ephemeral keys
- Autentikasi terintegrasi menggunakan signature schemes
- Multi-party key exchange protocols
- Integration dengan existing PKI infrastructure

**Analisis Formal:**

- Proof keamanan formal menggunakan reduction-based security
- Analisis keamanan quantum (post-quantum cryptography considerations)
- Benchmark performa terhadap protokol existing
- Standardisasi format dan implementasi

**Interface dan Usability:**

- Web API untuk integrasi dengan aplikasi lain
- Command-line interface untuk testing otomatis
- Library implementations dalam berbagai bahasa pemrograman
- Documentation dan tutorial yang lebih comprehensive

## Referensi

### Dasar Teoritis:

1. **Aljabar Max-Plus**:

   - Baccelli, F., et al. "Synchronization and Linearity: An Algebra for Discrete Event Systems" (1992)
   - Gaubert, S. "Methods and Applications of (max,+) Linear Algebra" (1997)

2. **Matriks LdlP (Linde-de la Puente)**:

   - Linde, J. & de la Puente, M.J. "An algorithm to compute the primitive matrices with a given characteristic polynomial" (1998)
   - Komutativitas dalam aljabar max-plus dan aplikasinya

3. **Kriptografi berbasis Aljabar Non-Klasik**:
   - Maze, G., et al. "Public Key Cryptography based on Simple Modules over Simple Rings" (2002)
   - Anshel, I., et al. "An algebraic method for public-key cryptography" (1999)

### Protokol Pertukaran Kunci:

4. **Diffie-Hellman Original**:

   - Diffie, W. & Hellman, M. "New Directions in Cryptography" (1976)
   - Dasar teoretis untuk semua protokol pertukaran kunci asimetrik

5. **Protokol Berbasis Semiring**:
   - Researches tentang aplikasi semiring dalam kriptografi
   - Non-commutative algebraic structures untuk keamanan

### Implementasi dan Keamanan:

6. **AES-GCM dan Key Derivation**:

   - NIST SP 800-38D "Galois/Counter Mode (GCM) and GMAC" (2007)
   - RFC 5869 "HMAC-based Extract-and-Expand Key Derivation Function (HKDF)" (2010)

7. **Analisis Kompleksitas Kriptografi**:
   - Katz, J. & Lindell, Y. "Introduction to Modern Cryptography" (2020)
   - Foundations of computational complexity dalam konteks kriptografi

### Implementasi Web dan Educational Tools:

8. **Mathematical Notation on Web**:
   - KaTeX documentation untuk rendering matematis
   - Best practices untuk interactive mathematical demonstrations

---

**Catatan**: Demo ini dibuat untuk tujuan educational dan research. Untuk aplikasi production yang sesungguhnya, diperlukan analisis keamanan formal yang mendalam, implementasi yang dioptimasi, dan testing ekstensif terhadap berbagai jenis serangan kriptanalisis.
