from manim import *
from manim_slides import Slide
from lib.slide_tracker import *

config.background_color = WHITE

class RevisionScene(Slide):
    def construct(self):
        animasi_pemilihan_B_star(self)

def animasi_pemilihan_B_star(s):
    Mobject.set_default(color=BLACK)
    
    # SLIDE 1: TAHAP ALTERNATIF
    judul_algo = Title("Algoritma Pencarian Pasangan Komutatif", color=BLACK, font_size=40, include_underline=True)
    judul_algo[-1].set_color(BLACK)
    s.play(Write(judul_algo))
    
    tex_alt = Tex(
        r"\parbox{" + str(config.frame_width) + r"cm}{"
        r"\textbf{Tahap 1: Pencarian Alternatif (Subgrup Abelian)}\\[0.3cm]"
        r"1. Dekomposisikan matriks $A$ menjadi himpunan permutasi penyusun $\Sigma_A = \{\sigma_1^A, \dots, \sigma_n^A\}$.\\[0.1cm]"
        r"2. Periksa apakah seluruh elemen $\Sigma_A$ saling komutatif. Jika saling komutatif, maka $\Sigma_A$ membangkitkan subgrup Abelian $H_A$.\\[0.1cm]"
        r"3. Untuk setiap permutasi pengacakan indeks $\pi \in S_n$, bentuk permutasi baru $\sigma_i^B = \sigma_{\pi(i)}^A$ untuk setiap $i \in \underline{n}$.\\[0.1cm]"
        r"4. Bentuk kandidat matriks $B$ dari kumpulan permutasi $\sigma_i^B$ tersebut.\\[0.1cm]"
        r"5. Simpan $B$ ke dalam himpunan solusi. Berdasarkan Teorema Subgrup Abelian, kandidat $B$ ini dijamin saling komutatif dengan $A$."
        r"}",
        color=BLACK, font_size=30
    ).next_to(judul_algo, DOWN, buff=0.5)
    
    s.play(Write(tex_alt), run_time=2.5)
    s.wait(1)
    
    try: s.next_slide()
    except: pass
    
    # SLIDE 2: TAHAP UMUM
    tex_umum = Tex(
        r"\parbox{" + str(config.frame_width) + r"cm}{"
        r"\textbf{Tahap 2: Pencarian Umum (Metode Backtrack)}\\[0.3cm]"
        r"1. Tentukan himpunan \textit{centralizer} $C_{S_n}(\sigma_n^A)$.\\[0.1cm]"
        r"2. Untuk setiap $\tau \in C_{S_n}(\sigma_n^A)$, tetapkan kandidat permutasi maksimum $\sigma_n^B = \tau$.\\[0.1cm]"
        r"3. Inisialisasi matriks parsial $B^*$ dengan menempatkan simbol $n$ sesuai permutasi $\sigma_n^B$.\\[0.1cm]"
        r"4. Lakukan penelusuran menurun secara \textit{backtrack} untuk $m = n-1, \dots, 2$:\\[0.1cm]"
        r"\hspace*{0.5cm}a. Uji setiap kandidat $\sigma_m^B \in S_n$ pada entri yang masih kosong di $B^*$.\\[0.1cm]"
        r"\hspace*{0.5cm}b. Jika syarat superlevel $\mathcal{U}_{\ge n+m}^{AB} = \mathcal{U}_{\ge n+m}^{BA}$ terpenuhi, simpan simbol $m$ dan lanjutkan ke langkah $m-1$.\\[0.1cm]"
        r"\hspace*{0.5cm}c. Jika ditolak, hapus kembali simbol $m$ dari $B^*$ dan uji $\sigma_m^B$ selanjutnya.\\[0.1cm]"
        r"5. Untuk tahap $m=1$, isi entri yang tersisa pada $B^*$ dengan simbol $1$ dan simpan ke himpunan solusi apabila matriks tersebut valid."
        r"}",
        color=BLACK, font_size=30
    ).next_to(judul_algo, DOWN, buff=0.5)
    
    s.play(FadeOut(tex_alt, shift=LEFT))
    s.play(FadeIn(tex_umum, shift=RIGHT))
    s.wait(1)
    
    try: s.next_slide()
    except: pass
    
    s.play(FadeOut(tex_umum, shift=LEFT))
    
    # SLIDE 3: ANIMASI PEMILIHAN B*
    judul_bstar = Title(r"Tahap Umum: Ilustrasi \textit{Backtrack}", color=BLACK, font_size=40, include_underline=True)
    judul_bstar[-1].set_color(BLACK)
    
    s.play(Transform(judul_algo, judul_bstar))
    
    b_star_mat = Matrix([
        [r"\varepsilon", r"\varepsilon", r"\varepsilon", r"\varepsilon", r"\varepsilon"],
        [r"\varepsilon", r"\varepsilon", r"\varepsilon", r"\varepsilon", r"\varepsilon"],
        [r"\varepsilon", r"\varepsilon", r"\varepsilon", r"\varepsilon", r"\varepsilon"],
        [r"\varepsilon", r"\varepsilon", r"\varepsilon", r"\varepsilon", r"\varepsilon"],
        [r"\varepsilon", r"\varepsilon", r"\varepsilon", r"\varepsilon", r"\varepsilon"]
    ], v_buff=0.7, h_buff=0.7).scale(0.7).set_color(BLACK).next_to(judul_bstar, DOWN, buff=1)
    
    for ent in b_star_mat.get_entries():
        ent.set_color(GRAY)
        
    lbl_B = MathTex("B^* =").scale(0.8).next_to(b_star_mat, LEFT)
    grp_mat = VGroup(lbl_B, b_star_mat).shift(DOWN*0.5)
    
    s.play(Write(lbl_B), Create(b_star_mat))
    
    tahapan = [
        {
            "m": 5,
            "teks": r"Kandidat $m=5$: Misal $\sigma_5^B = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 5 & 4 & 3 & 2 & 1 \end{pmatrix} \in C_{S_5}(\sigma_5^A)$",
            "pos": [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)],
            "col": PURE_RED
        },
        {
            "m": 4,
            "teks": r"Evaluasi $m=4$: Lolos syarat superlevel untuk $\sigma_4^B = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 2 & 1 & 5 \end{pmatrix}$",
            "pos": [(0, 3), (1, 2), (2, 1), (3, 0), (4, 4)],
            "col": ORANGE
        },
        {
            "m": 3,
            "teks": r"Evaluasi $m=3$: Lolos syarat superlevel untuk $\sigma_3^B = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 2 & 1 & 5 & 4 \end{pmatrix}$",
            "pos": [(0, 2), (1, 1), (2, 0), (3, 4), (4, 3)],
            "col": TEAL
        },
        {
            "m": 2,
            "teks": r"Evaluasi $m=2$: Lolos syarat superlevel untuk $\sigma_2^B = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 2 & 1 & 5 & 4 & 3 \end{pmatrix}$",
            "pos": [(0, 1), (1, 0), (2, 4), (3, 3), (4, 2)],
            "col": PURE_BLUE
        },
        {
            "m": 1,
            "teks": r"Evaluasi $m=1$: Sisa entri matriks otomatis membentuk permutasi $\sigma_1^B$.",
            "pos": [(0, 0), (1, 4), (2, 3), (3, 2), (4, 1)],
            "col": PURE_GREEN
        }
    ]
    
    prev_teks = None
    for step in tahapan:
        m = step["m"]
        teks_mob = Tex(step["teks"], font_size=32, color=BLACK).next_to(judul_bstar, DOWN, buff=0.4)
        
        if prev_teks:
            s.play(Transform(prev_teks, teks_mob))
        else:
            s.play(Write(teks_mob))
            prev_teks = teks_mob
            
        posisi = step["pos"]
        updates = []
        for r, c in posisi:
            idx = r * 5 + c
            target_entry = b_star_mat.get_entries()[idx]
            new_entry = MathTex(str(m), font_size=36).set_color(step["col"]).move_to(target_entry)
            updates.append(Transform(target_entry, new_entry))
            
        boxes = VGroup(*[SurroundingRectangle(b_star_mat.get_entries()[r*5+c], color=step["col"], buff=0.1) for r,c in posisi])
        
        s.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.1), run_time=0.6)
        s.play(LaggedStart(*updates, lag_ratio=0.2), run_time=1)
        s.play(FadeOut(boxes), run_time=0.4)
        s.wait(0.5)
        
    teks_final = Tex(r"Seluruh entri matriks telah terisi valid, kandidat $B^*$ disimpan ke $\mathcal{P}(A)$.", font_size=32, color=PURPLE_E).next_to(grp_mat, DOWN, buff=0.4)
    s.play(Write(teks_final))
    s.wait(2)
