# Claude.md - Project Context & Feature Tracker

## Project Overview
**Nama Proyek:** Pameran Tugas Akhir - Aplikasi Interaktif  
**Topik TA:** Latin Square Komutatif atas Aljabar Max-Plus  
**Tech Stack:** Next.js 16 (App Router) + TypeScript + Tailwind CSS v4 + KaTeX + Framer Motion  
**Deploy Target:** Vercel  
**Font:** Plus Jakarta Sans (body) + Libre Baskerville (headings/math context)  
**Math Rendering:** KaTeX

---

- Codex update: slide 3 dirombak total menjadi perbandingan perkalian matriks biasa vs aljabar max-plus. Sekarang ada dua mode interaktif, formula per entri, serta visual matriks A, B, dan hasil C agar pengunjung melihat bahwa bentuk matriks tetap sama meski aturan operasinya berubah.
- Codex update: ilustrasi slide 3 dibuat lebih interaktif dan ringkas. Matriks diperkecil, entri hasil C kini bisa diklik, lalu slide menyorot baris A dan kolom B yang dipakai serta menulis ulang ekspresi KaTeX yang berubah sesuai entri terpilih, dengan warna angka dibedakan antara matriks A dan B.
- Codex update: responsif slide 3 diperbaiki untuk HP. Susunan matriks interaktif sekarang menumpuk vertikal di layar kecil dan ukuran sel diperkecil agar ilustrasi tidak melebar keluar layar.
- Codex update: penamaan slide 3 dirapikan. Komponen yang tadinya masih bernama `ResearchDecompositionSlide` dipindah menjadi `MatrixMultiplicationSlide` agar isi slide dan nama file sekarang sejalan. Sizing matriks juga tidak lagi memakai `max-w-[110px]`, tetapi mengikuti ukuran sel responsif yang lebih natural.
- Codex update: penamaan slide 2 ikut dirapikan. Komponen `ResearchOverviewSlide` dipindah menjadi `LatinSquareSlide` agar nama file langsung sesuai dengan isi slide tentang Latin square.
- Codex update: visual slide 3 dirapikan lagi sesuai feedback. Ilustrasi interaktif kini dipertahankan kiri-ke-kanan dalam satu baris dengan `overflow-x-auto` saat layar sempit, tampilan matriks diganti ke bracket matriks sungguhan, dan card info dibuat `min-w-0` plus scroll horizontal pada blok KaTeX supaya konten tidak lagi kepotong.
- Codex update: slide 3 kini disamakan pola visualnya dengan slide 1 dan 2. Heading, body text, wrapper, ritme card, dan `motion` container/item sekarang memakai struktur yang konsisten dengan dua slide sebelumnya.
- Codex update: controller progress di bagian atas dipisahkan dari animasi pergantian slide, jadi tidak ikut hilang saat navigasi. Slide 4 sampai 7 juga ditarik ke pola heading, body text, dan `motion` yang sama seperti slide 1 dan 2 agar tampil lebih konsisten.
- Codex update: garis samping pseudo pada visual matriks slide 3 dihapus. Ilustrasi interaktif sekarang lebih bersih tanpa bracket samping tambahan yang tidak membantu pembacaan.
- Codex update: perpindahan mode di `MatrixMultiplicationSlide` dibuat lebih halus di atas struktur file terbaru. Bagian penjelasan dan ilustrasi sekarang memakai crossfade dengan sedikit gerak dan scaling saat berpindah antara aljabar biasa dan max-plus.
- Codex update: perpindahan mode pada slide 3 kini dianimasikan lebih halus. Saat ganti antara aljabar biasa dan max-plus, panel penjelasan dan ilustrasi matriks sekarang saling menimpa lewat crossfade dengan sedikit gerak dan scaling agar transisinya tidak terasa kaku.
- Codex update: animasi ganti mode di slide perkalian matriks diperhalus lagi di atas file terbaru. Transisi kini punya arah kiri-kanan, blur halus, dan dorongan scale yang lebih terasa supaya pergantian aljabar biasa dan max-plus tidak lagi kaku.
- Codex update: mode transisi slide perkalian matriks dirapikan lagi agar tidak memunculkan dua komponen sekaligus. `AnimatePresence` untuk panel kiri dan ilustrasi kanan kini memakai `mode="wait"` supaya card tidak membesar aneh saat perpindahan mode.
- Codex update: slide perkalian matriks disetel lagi setelah review visual. Durasi transisi mode dipercepat, blur dan gesernya diperingan, scrollbar flash pada area ilustrasi disembunyikan, dan sel `C` yang dipilih kini memakai hijau yang lebih tegas agar state aktifnya benar-benar terlihat.
- Codex update: revisi lanjutan pada slide perkalian matriks dibuat lebih tegas. Overflow ilustrasi kini benar-benar di-hide agar scrollbar transien tidak muncul, durasi transisi mode dipotong lagi supaya lebih sigap, dan sel `C` aktif sekarang diberi hijau solid plus ring agar highlight kliknya tidak samar.
- Codex update: state selected pada matriks `C` dikoreksi lagi. Teks putih pada sel aktif ternyata membuat angka terasa hilang, jadi warna selected diubah ke `bg-emerald-300` dengan teks gelap agar highlight tetap hijau tetapi angkanya jelas terbaca.
- Codex update: contoh pada slide perkalian matriks diperbesar ke matriks `3x3`. Matriks `A`, `B`, hasil aljabar biasa, hasil max-plus, dan ekspresi KaTeX saat klik entri kini semuanya ikut dihitung ulang untuk tiga suku.
- Codex update: warna selected pada entri aktif matriks `C` ditegaskan lagi. Background state klik sekarang dinaikkan ke `bg-emerald-500` supaya sel yang sedang dipilih benar-benar terbaca hijau aktif, sementara teks tetap gelap.
- Codex update: highlight entri aktif matriks `C` diperbaiki lagi. Hover state pada sel interaktif ternyata bisa menimpa warna selected, jadi sekarang hover dinonaktifkan untuk sel yang sedang aktif dan class selected emerald dipaksa dengan `!bg-emerald-500`.
- Codex update: slide 4 dirapikan ulang menjadi accordion native berbasis `details/summary`. Bagian syarat perlu, syarat cukup, dan perlu-cukup kini membuka kontennya ke bawah saat diklik, sementara blok “Kenapa ini kuat” dihapus agar isi slide lebih fokus.
- Codex update: arah materi slide 3 diganti. `MatrixMultiplicationSlide` sekarang tidak lagi membahas perkalian biasa vs max-plus, tetapi hubungan Latin square dengan matriks permutasinya berdasarkan bab 2 dan bab 4: dekomposisi simbol ke matriks permutasi max-plus serta aksi perkalian kiri/kanan oleh matriks permutasi yang tetap menjaga sifat Latin square. Label navigasinya juga diubah dari `Perkalian` menjadi `Permutasi`.
- Codex update: seluruh file slide direname agar nama file langsung menjelaskan isi slide. Contohnya `SudokuSlide` menjadi `SudokuPuzzleSlide`, `LatinSquareSlide` menjadi `LatinSquareConceptSlide`, `MatrixMultiplicationSlide` menjadi `LatinSquarePermutationSlide`, serta slide-slide hasil lainnya ikut disesuaikan dan import di `page.tsx` diperbarui.
- Codex update: materi permutasi pada slide 3 dipecah lagi menjadi dua slide terpisah. `LatinSquareDecompositionSlide` kini khusus untuk dekomposisi Latin square ke matriks permutasi max-plus, sedangkan `PermutationMatrixActionSlide` khusus untuk aksi perkalian kiri/kanan oleh matriks permutasi. Navigasi slide juga ditambah satu langkah baru: `Dekomposisi` lalu `Aksi Permutasi`.
- Codex update: puzzle Latin square sekarang lengkap punya pilihan ordo 3, ordo 4, dan ordo 5 pada versi interaktifnya. Sekalian posisi slide aktif kini disimpan di `localStorage`, jadi refresh tidak lagi melempar pengunjung balik ke slide awal.
- Codex update: clue awal puzzle Latin square tidak lagi memakai pola diagonal tetap. Givens sekarang dibangkitkan acak dari solusi masing-masing ordo dengan sebaran baris/kolom yang lebih natural.
- Codex update: badge huruf pada aturan Latin square diperjelas. Styling `bg-sky-*` yang nyaris tak terbaca di latar putih diganti menjadi badge `inline-flex` dengan `border-sky-200`, `bg-sky-100`, dan teks `sky-800`.
- Codex update: logic conflict pada puzzle Sudoku dan Latin square dirapikan. Sel merah sekarang hanya muncul sementara pada cluster benturan yang aktif lalu hilang otomatis setelah sekitar 1,6 detik atau saat pemain pindah seleksi, sehingga board tidak menumpuk merah terus. Clue bawaan yang ikut bentrok juga dibedakan dengan merah yang lebih gelap agar lebih mudah dibaca.
- Codex update: dev server Next 16 dikonfigurasi untuk mengizinkan origin `127.0.0.1` lewat `allowedDevOrigins` di `next.config.ts`. Ini memperbaiki blokir HMR/WebSocket saat aplikasi dibuka dari `http://127.0.0.1:3000` alih-alih `localhost`.
- Codex update: mismatch hidrasi di `page.tsx` dibereskan. State opening screen dan slide aktif tidak lagi dibaca dari `localStorage` saat render awal, tetapi baru disinkronkan setelah mount, sehingga HTML server dan render client pertama tetap sama.
- Codex update: fase bootstrap `page.tsx` sekarang punya shell awal dengan spacing yang sama seperti slide utama. Jadi sebelum state lokal selesai disinkronkan, halaman tidak lagi tampil rapet atau terasa seperti margin/padding hilang.
- Codex update: atas permintaan rollback, rangkaian perubahan setelah revisi logic puzzle dibatalkan. Puzzle Sudoku dan Latin square dikembalikan ke perilaku conflict sebelumnya, sementara `page.tsx` dan `next.config.ts` juga dipulangkan ke versi sebelum eksperimen bootstrap/hidrasi/HMR belakangan.
- Codex update: repo git lokal baru diinisialisasi langsung di folder `Pameran TA` dan snapshot awal proyek sudah dikomit agar perubahan berikutnya bisa di-undo dengan rapi dari level folder ini.
- Codex update: visual slide 1-3 dirapikan tanpa mengubah tipografi inti. Masalah utamanya bukan Tailwind/global CSS rusak, melainkan ruang atas-bawah slide terlalu mepet terhadap navbar fixed dan tombol navigasi fixed. Wrapper slide 1-3 sekarang diberi `pt` dan `pb` lebih lega serta `gap` antarblok dikembalikan agar konten tidak tampak rapet atau tertindih.
- Codex update: visual conflict Sudoku disetel lagi. Sel input pemain yang benar-benar bentrok sekarang tetap merah walau feedback cluster sekitarnya sudah memudar, sedangkan highlight biru untuk clue bawaan yang ikut tersorot dibuat sedikit lebih gelap agar lebih gampang dibedakan dari sel biasa.
- Codex update: contoh KaTeX Latin square di slide 2 diperkecil lagi. Font matriks contoh sekarang lebih kecil dan padding kartu contoh sedikit diringkas supaya blok contoh tidak terasa kebesaran dibanding isi slide lainnya.
- Codex update: slide 3 tentang perbandingan Aljabar Biasa vs Aljabar Max-Plus dipulihkan sebagai file baru `BasicVsMaxPlusSlide.tsx`, lalu disisipkan kembali di antara slide Latin square dan dekomposisi. Urutan navigasi kini kembali punya langkah `Perkalian` sebelum masuk ke matriks permutasi max-plus.
- Codex update: slide 3 perbandingan operasi dipulihkan lagi dengan nama yang lebih sesuai jejak lama, yaitu `MatrixMultiplicationSlide.tsx`. Isinya sekarang kembali ke bentuk interaktif: mode `Aljabar Biasa` vs `Aljabar Max-Plus`, matriks `A`, `B`, dan `C` yang bisa diklik pada entri hasil, highlight baris/kolom sumber, serta ekspresi KaTeX yang berubah mengikuti entri terpilih.
- Codex update: puzzle Latin square di slide 2 diperkecil lagi supaya proporsinya lebih selaras dengan contoh dan teks pada slide itu. Lebar maksimum grid untuk ordo 3/4/5 diturunkan, dan ukuran font sel juga diringankan agar papan tidak terasa terlalu besar.
- Codex update: sizing puzzle Latin square dirapikan lagi agar lebih dekat proporsinya ke Sudoku. Nested ternary untuk lebar grid dan ukuran font sel diganti menjadi config per ordo yang lebih bersih, ukuran papan dikecilkan lagi, dan wrapper header puzzle dibetulkan menjadi `flex flex-col` supaya layout kontrolnya lebih rapi.
- Codex update: warning canonical Tailwind di `page.tsx` dibersihkan. Kelas background gradient pembuka, arah gradient loading bar, dan radius kartu opening diganti ke bentuk canonical yang disarankan Tailwind IntelliSense tanpa mengubah tampilan.
- Codex update: warning canonical Tailwind di `LatinSquarePuzzle.tsx` dibersihkan juga. Posisi confetti dan lapisan overlay sukses kini memakai bentuk kelas canonical (`-top-3`, `z-300`, `z-200`) tanpa mengubah perilaku visual.

## Design Philosophy
- Warm academic palette: parchment, ink, gold, emerald.
- Interactive slides with small, focused learning steps.
- Micro-animations via Framer Motion.
- Editorial layout with readable typography and restrained controls.
- Sudoku first, Latin Square after the puzzle, Max-Plus after the base concept is clear.

---

## Current Flow

### Completed
- [x] **Slide 0 - Pola Sudoku**
  - Intro tentang cara membaca pola Sudoku.
  - Aturan baris, kolom, dan region 3x3.
  - Visual preview grid Sudoku.
  - Ornamen matematika: graf, matriks, region grid, dan formula kecil.

- [x] **Slide 1 - Puzzle Sudoku**
  - Sudoku standar 9x9 dengan region 3x3.
  - Puzzle dibuat mudah dengan banyak angka awal.
  - Angka pre-filled tidak bisa diedit.
  - Input 1-9 via number pad dan keyboard.
  - Highlight baris, kolom, dan region dibuat lembut agar angka tetap terbaca.
  - Conflict state tetap merah.
  - Success overlay setelah puzzle selesai.
  - Setelah selesai, unlock slide berikutnya.

- [x] **Slide 2 - Latin Square**
  - Pengantar dari Sudoku ke Latin Square.
  - Bentuk formal sederhana dengan KaTeX.
  - Visual Latin Square 4x4.

- [x] **Slide System**
  - Progress dots di top bar.
  - Lock mechanism.
  - Prev/Next navigation buttons.
  - Animasi transisi antar slide.

### Planned
- [ ] **Slide 3 - Aljabar Max-Plus**
  - Kalkulator interaktif max-plus.

- [ ] **Slide 4 - Latin Square di Aljabar Max-Plus**
  - Visualisasi matriks dan sifat komutatif.

- [ ] **Slide 5 - Eigenvalue & Eigenvector**
  - Simulasi step-by-step.

- [ ] **Slide 6 - Kesimpulan**

---

## Technical Decisions

| Keputusan | Pilihan | Alasan |
|-----------|---------|--------|
| Framework | Next.js 16 (App Router) | SSR, Vercel-native |
| Styling | Tailwind CSS v4 | CSS-first config |
| Math | KaTeX | Rendering sinkronus |
| Font Body | Plus Jakarta Sans | Humanistik |
| Font Heading | Libre Baskerville | Scholarly, warm |
| Animation | Framer Motion | Smooth, deklaratif |
| Sudoku | 9x9 standard | Region 3x3 valid untuk Sudoku penuh |

---

## File Structure
```txt
src/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
├── components/
│   ├── SlideController.tsx
│   ├── Sudoku/
│   │   ├── SudokuGrid.tsx
│   │   ├── SudokuSlide.tsx
│   │   └── sudokuUtils.ts
│   ├── slides/
│   │   └── IntroSlide.tsx
│   └── ui/
│       └── MathBlock.tsx
├── postcss.config.mjs
└── claude.md
```

---

## Changelog

### 2026-06-06
- Codex update: isi pameran diperluas agar benar-benar membawa hasil TA, bukan sekadar pengantar Sudoku dan satu slide formal Latin Square.
- Codex update: setelah slide Sudoku yang sudah ada, ditambahkan rangkaian slide baru berbasis hasil laporan: `Masalah`, `Dekomposisi`, `Kriteria`, `Algoritma`, `Contoh`, dan `Manfaat`.
- Codex update: tiap slide baru dibuat interaktif lewat tab, selector, atau stepper agar pengunjung bisa mengeksplorasi masalah penelitian, dekomposisi Latin square, syarat komutatif, alur algoritma, dan contoh hasil ordo 3/4/5.
- Codex update: contoh konkret pada slide hasil diambil dari laporan `Laporan TA/Inti`, termasuk pasangan Latin square komutatif dan hasil perkalian max-plus untuk ordo 3, 4, dan 5.
- Codex update: flow presentasi kini diarahkan per ide besar, bukan per bab laporan, supaya pengunjung lebih mudah menangkap manfaat dan kontribusi tugas akhir.
- Verifikasi: `pnpm lint` dan `pnpm build` lolos setelah penambahan slide hasil TA.
- Codex update: opening screen ditambahkan sebelum slide dengan loading singkat, reveal identitas tugas akhir, dan prompt lanjut.
- Codex update: opening screen sekarang diingat lewat `localStorage`, sehingga refresh biasa tidak mengulang intro. Intro akan muncul lagi setelah jeda kunjungan yang dianggap lama.
- Codex update: ditambahkan screen pembuka full-screen sebelum slide dengan animasi loading, data tugas akhir, dan teks berkedip untuk lanjut.
- Codex update: slide pengantar Sudoku dan puzzle digabung ke satu halaman bergaya artikel, sementara blok aturan dipertahankan apa adanya.
- Codex update: file `src/components/slides/SudokuSlide.tsx` disinkronkan dengan layout aktif agar tidak ada perbedaan antara file yang dipakai dan file yang diedit.
- Verifikasi: `pnpm lint` dan `pnpm build` lolos.

### 2026-06-05
- Codex update: modal sukses kini ditutup dengan klik area mana saja. Tombol `Tutup` dihapus, dan verifikasi `pnpm lint` serta `pnpm build` tetap lolos.
- Codex update: modal sukses disederhanakan lagi. Tombol `Tutup` akan dihapus dan overlay akan bisa ditutup cukup dengan klik area mana saja.
- Codex update: modal `Puzzle Selesai` kini bisa ditutup manual lewat tombol `Tutup`. Menutup modal juga tetap memastikan slide berikutnya terbuka. Verifikasi `pnpm lint` dan `pnpm build` lolos.
- Codex update: perbaikan modal sukses dimulai. Overlay `Puzzle Selesai` akan dibuat bisa ditutup manual tanpa mengganggu proses unlock slide berikutnya.
- Codex update: slide 2 ditambah puzzle Latin square interaktif. Pengunjung sekarang bisa menyusun matriks dari angka yang sudah diberikan dengan interaksi mirip Sudoku, lengkap pilihan contoh ordo 3 dan ordo 5, highlight baris/kolom, hint, penanda benar, dan tombol selesaikan.
- Codex update: grid aturan slide 2 disetel ulang. Dua kartu aturan Latin square sekarang pindah ke dua kolom mulai lebar `520px` lewat `min-[520px]:grid-cols-2`, jadi tidak perlu menunggu breakpoint `sm` penuh.
- Codex update: layout slide 2 disamakan penuh dengan slide 1. `ResearchOverviewSlide` sekarang memakai struktur centered stack, ritme spacing, animasi motion, dan bentuk card yang sama seperti `SudokuSlide`, hanya kontennya yang khusus menjelaskan Latin square.
- Codex update: responsif slide 2 dirapikan mengikuti slide 1. Heading dan intro sekarang center di mobile, ukuran font mobile dikecilkan, dan padding card dibuat lebih ringan agar tampilan HP tidak terasa terlalu besar.
- Codex update: slide 2 direvisi menjadi pengantar Latin square. Isinya sekarang menjelaskan bahwa Latin square mirip Sudoku, tetapi aturan region 3x3 dihapus, lengkap dengan contoh 4x4 dan ringkasan transisinya ke topik penelitian.
- Codex update: fitur bantuan puzzle selesai. Ditambahkan tombol `Hint` untuk mengisi satu sel acak dengan jawaban benar lalu menguncinya, tombol `Selesaikan` untuk membuka seluruh solusi, dan penanda hijau khusus untuk input pemain yang benar. Verifikasi `pnpm lint` dan `pnpm build` lolos.
- Codex update: fitur bantuan puzzle dimulai. Akan ditambahkan `Hint` untuk mengisi satu sel acak dan menguncinya, `Selesaikan` untuk membuka seluruh solusi, serta penanda hijau khusus untuk input pemain yang benar.
- Codex update: behavior conflict diperluas. State conflict pada Sudoku tidak lagi dibatasi untuk sel non-given, sehingga semua angka duplikat di baris, kolom, atau region yang bentrok ikut merah dan ikut shake. Verifikasi `pnpm lint` dan `pnpm build` lolos.
- Codex update: behavior conflict sedang diperluas. Semua sel yang punya angka sama dalam baris, kolom, atau region yang bentrok akan ikut masuk state conflict dan ikut shake, termasuk sel given bila terkena benturan.
- Codex update: animasi sisa pada sel Sudoku dibersihkan. Transisi warna di sel dihapus, animasi angka saat render dihapus, dan motion pada sel kini hanya aktif untuk conflict shake. Verifikasi `pnpm lint` dan `pnpm build` lolos.
- Codex update: style angka input user distabilkan. Class `font-extrabold text-emerald-700` tidak lagi hilang saat sel dipilih, jadi select dan unselect tidak membuat angka berubah tampilan. Verifikasi `pnpm lint` dan `pnpm build` tetap lolos.
- Codex update: interaksi mobile Sudoku diperbaiki. Efek `whileTap` pada sel grid dihapus dan `touch-manipulation` ditambahkan agar tap select/unselect tidak terasa seperti zoom. Verifikasi `pnpm lint` dan `pnpm build` tetap lolos.
- Codex update: perbaikan interaksi mobile dimulai. Efek tap pada sel Sudoku sedang dirapikan agar select dan unselect tidak terasa seperti zoom in zoom out di layar kecil.
- Codex update: fitur unselect grid selesai. Sel aktif sekarang bisa dibatalkan dengan klik ulang pada sel yang sama. Verifikasi `pnpm lint` dan `pnpm build` tetap lolos.
- Codex update: penambahan fitur unselect grid dimulai. Targetnya sel aktif bisa dibatalkan dengan klik ulang agar interaksi Sudoku terasa lebih natural.
- Codex update: koreksi helper state Sudoku selesai. `getCellStyle` kembali menjadi sumber utama untuk selected/highlight/conflict, dan kini memakai `backgroundColor` (`amber-300`, `sky-200`, `rose-200`) alih-alih shadow.
- Codex update: koreksi state helper Sudoku dimulai. Blok `getCellStyle` yang mengatur state visual dikembalikan sebagai sumber utama, tetapi kini memakai `backgroundColor` alih-alih `boxShadow`.
- Codex update: state visual Sudoku direvisi lagi. Shadow pada selected/highlight/conflict dihapus; selected kini `bg-amber-300`, highlight area menjadi `bg-sky-200`, dan conflict menjadi `bg-rose-200`.
- Codex update: revisi state highlight dimulai. Shadow pada state Sudoku akan dihapus, lalu selected/highlight/conflict dibuat murni berbasis background color. Highlight emerald diganti ke sky sesuai arahan terbaru.
- Codex update: refactor styling selesai. `globals.css` sekarang hanya import Tailwind, sementara style custom Sudoku, ornament motion, confetti, dan heading font dipindah ke file `.tsx` masing-masing. `pnpm lint` dan `pnpm build` lolos setelah perubahan ini.
- Codex update: refactor styling dimulai sesuai arahan baru. Semua style custom sedang dipindah keluar dari `globals.css` ke file komponen `.tsx`, termasuk Sudoku state, ornament animation, dan font heading helper.
- Codex update: verifikasi migrasi warna berhasil. `pnpm lint` dan `pnpm build` lolos setelah semua pemakaian hex/rgba/arbitrary color dibersihkan dari `src`.
- Codex update: warna UI dimigrasi dari hex/custom palette ke Tailwind default palette. Mapping utama: parchment -> stone, ink -> stone, gold -> amber; hex/rgba/arbitrary color sudah tidak ditemukan di `src`.
- Codex update: revisi warna dimulai. Target: hapus pemakaian kode hex langsung pada komponen/CSS dan ganti ke class Tailwind atau variable theme yang sudah ada.
- Codex update: slide 2 sekarang punya blok contoh statis Latin square dengan KaTeX untuk ordo 3, ordo 4, dan ordo 5 secara berurutan. Contoh lama ordo 4 dikembalikan, sementara puzzle interaktif tetap ada di bawahnya.
- Codex update: verifikasi revisi terbaru berhasil. `pnpm lint` dan `pnpm build` lolos setelah perubahan preview Sudoku dan highlight.
- Codex update: slide pertama diperbarui menjadi penjelasan saja dengan preview Sudoku lebih kecil dan seluruh kotak terisi. Highlight puzzle dinaikkan kontrasnya: selected cell lebih gold, row/column/region lebih emerald.
- Codex update: revisi lanjutan dimulai. Slide pertama akan dibuat sebagai penjelasan Sudoku saja, preview grid diperkecil dan diisi penuh. Slide puzzle akan memakai highlight row/column/region yang lebih kontras.
- Codex update: verifikasi revisi lanjutan berhasil. `pnpm lint` dan `pnpm build` sama-sama lolos.
- Codex update: slide awal ditambah penjelasan definisi dan tujuan Sudoku. Preview grid diperbaiki memakai inline `gridTemplateColumns` agar selalu 9 kolom. Highlight Sudoku diperkuat dengan warna emerald transparan dan selected cell gold yang lebih jelas.
- Codex update: revisi lanjutan dimulai. Fokus: highlight Sudoku dibuat lebih terlihat, preview grid di slide awal diperbaiki agar benar-benar 9 kolom, dan slide awal ditambah penjelasan Sudoku yang lebih lengkap.
- Codex update: revisi selesai dan dev server terkonfirmasi hidup di `http://127.0.0.1:3000` dengan status 200.
- Codex update: `claude.md` dibersihkan penuh dari mojibake dan diperbarui sesuai flow terbaru.
- Codex update: verifikasi berhasil. Tidak ada sisa mojibake di `src`, `pnpm lint` lolos, dan `pnpm build` lolos.
- Codex update: `SlideController` dan layout metadata dibersihkan dari mojibake.
- Codex update: `page.tsx` diganti bersih. Urutan slide kini Pola Sudoku -> Puzzle Sudoku -> Latin Square.
- Codex update: `SudokuSlide` diperbarui menjadi "Sudoku 9x9 Mudah" dengan aturan baris, kolom, dan region 3x3.
- Codex update: `IntroSlide` dibangun ulang sebagai pengantar Sudoku, bukan definisi Latin Square/Max-Plus.
- Codex update: `globals.css` dibersihkan dari mojibake dan style Sudoku diperbarui.
- Codex update: `SudokuGrid` diubah ke 9x9 standar, input 1-9, highlight dibuat ringan, dan lint React 19 dibereskan.
- Codex update: `sudokuUtils` diganti dari 6x6 blok 2x3 ke Sudoku standar 9x9 blok 3x3 dengan puzzle yang lebih mudah.
- Inisialisasi project Next.js 16 + TypeScript.
- Install: tailwindcss v4, katex, framer-motion.
- Setup fonts: Plus Jakarta Sans + Libre Baskerville.
- Implementasi slide system dengan lock mechanism.
- Codex update: merapatkan jarak antar matriks di slide perbandingan operasi dan membuat operator produk berganti dinamis antara `\times` dan `\otimes` di `src/components/slides/MatrixMultiplicationSlide.tsx`.
- Codex update: merevisi slide dekomposisi agar interaksi pindah ke contoh Latin square langsung; simbol kini dibedakan warnanya dan saat diklik baru dijelaskan permutasi yang ditunjukkan di `src/components/slides/LatinSquareDecompositionSlide.tsx`.
- Codex update: menyempurnakan slide dekomposisi dengan narasi yang lebih tepat secara konsep, state awal Latin square yang netral sebelum dipilih, warna matriks permutasi yang mengikuti simbol aktif, layout dua kolom, ukuran matriks yang diperbesar, dan perbaikan judul `P_{\sigma_i}` agar tidak berubah jadi Sigma kapital di `src/components/slides/LatinSquareDecompositionSlide.tsx`.
- Codex update: slot slide 5 diganti dari aksi permutasi menjadi materi reduksi dekomposisi hasil perkalian dua Latin square berdasarkan `bab 4.tex`, lalu file direname menjadi `src/components/slides/LatinSquareProductReductionSlide.tsx` dan label navigasinya diubah menjadi `Reduksi`.
- Codex update: slide kriteria kini memakai area scroll internal dengan scrollbar disembunyikan, jadi saat `details` dibuka tetap bisa digeser di mobile tanpa menampilkan scrollbar kanan halaman di `src/components/slides/CommutativityCriteriaSlide.tsx`.
- Codex update: memendekkan blok penjelasan reduksi agar KaTeX hanya dipakai untuk rumus, sementara uraian panjang dipindah ke teks HTML biasa, dan scrollbar visual pada container overflow slide reduksi serta slide kriteria disembunyikan di `LatinSquareProductReductionSlide.tsx` dan `CommutativityCriteriaSlide.tsx`.
- Codex update: slide reduksi dirombak jadi lebih ringkas dan web-like; KaTeX kini hanya dipakai untuk simbol/rumus singkat, ditambah visualisasi interaktif ordo 4 untuk memilih baris A dan kolom B lalu menampilkan penjumlahan per entri yang selalu memberi nilai minimal n+1, serta scrollbar visual viewport utama disembunyikan di `page.tsx`.
- Codex update: membersihkan teks slide reduksi dari karakter rusak hasil encoding dan merapikan penulisan batas bawah agar aman dipakai di HTML biasa.
- Codex update: mengembalikan bagian atas slide reduksi ke versi rumus sebelumnya sesuai arah user, sambil mempertahankan visualisasi interaktif ordo 4 di bagian bawah.
- Codex update: slide prosedur konstruksi diubah menjadi accordion yang memvisualisasikan pembentukan kandidat parsial `B*` hingga menjadi Latin square `B` secara bertahap di `src/components/slides/CommutativeSearchAlgorithmSlide.tsx`.
- Codex update: slide prosedur konstruksi kini menampilkan centralizer secara eksplisit pada tahap pemilihan simbol maksimum, sehingga sumber kandidat awal untuk `\sigma_n^B` terlihat jelas di `src/components/slides/CommutativeSearchAlgorithmSlide.tsx`.
- Codex update: slide prosedur konstruksi kini menjadi visualizer yang menampilkan Latin square `A` yang bisa diedit, menghitung `\sigma_4^A`, menurunkan centralizer yang bisa dipilih, lalu memperbarui alur `B* \to B` sesuai kandidat centralizer aktif di `src/components/slides/CommutativeSearchAlgorithmSlide.tsx`.
- Codex update: tampilan centralizer pada slide prosedur konstruksi dipendekkan dengan mengganti formula himpunan yang panjang menjadi label KaTeX singkat dan box-box kandidat KaTeX yang bisa dipilih di `src/components/slides/CommutativeSearchAlgorithmSlide.tsx`.
- Codex update: visualizer prosedur konstruksi kini menambahkan opsi permutasi lanjutan untuk `sigma_3^B` dan `sigma_2^B`, sehingga pengunjung bisa melihat bahwa simbol berikutnya juga punya beberapa kandidat yang ditentukan oleh posisi tersisa dan pemeriksaan superlevel.
- Codex update: visualizer prosedur konstruksi dirapikan lagi agar alurnya lebih kebaca. Ringkasan pilihan aktif untuk `sigma_4^B`, `sigma_3^B`, dan `sigma_2^B` sekarang dipisah di panel atas, sedangkan tombol kandidat permutasi dipindah ke accordion tahap masing-masing berikut penjelasan penyaring algoritmiknya: centralizer untuk simbol maksimum, lalu kandidat posisi kosong + cek `U_{>=7}` dan `U_{>=6}` untuk simbol berikutnya.
- Codex update: state awal visualizer prosedur konstruksi kini dibuat netral. `sigma_4^B`, `sigma_3^B`, dan `sigma_2^B` tidak lagi otomatis terpilih saat slide dibuka, kandidat aktif bisa dikosongkan kembali dengan klik ulang, dan tahap akhir tidak lagi menampilkan `B` penuh sebelum semua permutasi yang dibutuhkan benar-benar dipilih.
- Codex update: error type pada visualizer prosedur konstruksi dibersihkan dengan helper konversi aman untuk tuple `Permutation`, jadi cast `number[]` tidak lagi mentah. Slide penutup juga diarahkan ulang ke motivasi kriptografi: hasil penelitian ini diposisikan sebagai fondasi untuk skema mirip Diffie-Hellman Key Exchange dengan elemen berupa Latin square dan operasi max-plus.
- Codex update: urutan presentasi dipendekkan jadi 8 slide. Slot `Contoh` dihapus dari `page.tsx`, sehingga slide penutup `Manfaat` sekarang langsung menjadi slide ke-8 tanpa mengubah isi slide-slide lainnya.
- Codex update: kegagalan build Vercel pada `composePermutations` dibereskan. Permutasi sekarang dibentuk lewat helper tuple `toPermutation`, jadi hasil `map` tidak lagi dicast mentah dari array biasa ke `Permutation` dan pengecekan strict TypeScript saat build bisa lolos.
- Codex update: error build strict berikutnya di slide prosedur juga dibersihkan. `stepsMeta` sekarang diberi tipe eksplisit dengan `formula?: string`, sehingga akses `step.formula` tidak lagi bentrok dengan union literal saat build Vercel.
- Codex update: pengetikan `stepsMeta` di slide prosedur diwiden lagi menjadi `readonly StepMeta[]`, bukan hanya `satisfies`, supaya TypeScript build mode benar-benar mengakui `formula` sebagai properti opsional di semua step.
