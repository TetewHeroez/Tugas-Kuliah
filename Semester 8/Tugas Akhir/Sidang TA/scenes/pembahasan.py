from manim import *

from lib.slide_tracker import *


def pembahasan(s):
    s.play(
    s.camera.frame.animate
    .move_to(ORIGIN)
    .set(width=config.frame_width)
    .set_rotation(0), 
    run_time=1.5
    )
    SifatPerkalian(s)
    next_slide_count(s)
    InvariansiLatinSquare(s)
    next_slide_count(s)
    SyaratPerlu(s)
    next_slide_count(s)
    SyaratCukup(s)
    next_slide_count(s)
    RepresentasiKoordinat(s)
    next_slide_count(s)
    HimpunanSuperlevel(s)
    next_slide_count(s)
    TeoremaSuperlevel(s)
    next_slide_count(s)
    AlgoritmaKomutatif(s)
    next_slide_count(s)

def AlgoritmaKomutatif(s):
    Mobject.set_default(color=BLACK)

    judul_algo = Title("Algoritma Pencarian Pasangan Komutatif", color=BLACK, font_size=48, include_underline=True)
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
    s.next_slide()
    
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
    s.next_slide()
    
    s.play(FadeOut(tex_umum, shift=LEFT))
    
    def get_max_plus_product(mat1, mat2):
        res = [[None]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                m_val = None
                for k in range(5):
                    if mat1[i][k] is not None and mat2[k][j] is not None:
                        val = mat1[i][k] + mat2[k][j]
                        if m_val is None or val > m_val:
                            m_val = val
                res[i][j] = m_val
        return res

    A_vals = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 1],
        [3, 4, 5, 1, 2],
        [4, 5, 1, 2, 3],
        [5, 1, 2, 3, 4]
    ]
    B_vals = [[None]*5 for _ in range(5)]
    
    mat_A = Matrix([
        [str(x) for x in row] for row in A_vals
    ], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(0.5).set_color(BLACK)
    for ent in mat_A.get_entries(): ent.set_color(BLACK)
    lbl_A = MathTex("A =").scale(0.6)
    grp_A = VGroup(lbl_A, mat_A).arrange(RIGHT, buff=0.1)
    
    b_star_mat = Matrix([
        [r"\varepsilon"]*5 for _ in range(5)
    ], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(0.5).set_color(BLACK)
    for ent in b_star_mat.get_entries(): ent.set_color(GRAY)
    lbl_B = MathTex("B^* =").scale(0.6)
    grp_B = VGroup(lbl_B, b_star_mat).arrange(RIGHT, buff=0.1)
    
    grp_left = VGroup(grp_A, grp_B).arrange(DOWN, buff=0.4, aligned_edge=RIGHT)
    
    mat_AB = Matrix([
        [r"\varepsilon"]*5 for _ in range(5)
    ], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(1).set_color(BLACK)
    for ent in mat_AB.get_entries(): ent.set_color(GRAY)
    lbl_AB = MathTex("AB^*").scale(0.7)
    grp_AB = VGroup(lbl_AB, mat_AB).arrange(DOWN, buff=0.2)
    
    mat_BA = Matrix([
        [r"\varepsilon"]*5 for _ in range(5)
    ], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(1).set_color(BLACK)
    for ent in mat_BA.get_entries(): ent.set_color(GRAY)
    lbl_BA = MathTex("B^*A").scale(0.7)
    grp_BA = VGroup(lbl_BA, mat_BA).arrange(DOWN, buff=0.2)
    
    grp_right = VGroup(grp_AB, grp_BA).arrange(RIGHT, buff=0.6)
    
    grp_all = VGroup(grp_left, grp_right).arrange(RIGHT, buff=1.2, aligned_edge=UP).next_to(judul_algo, DOWN, buff=1)
    
    s.play(Write(grp_all), run_time=0.5)
    
    tahapan = [
        {
            "m": 5,
            "teks": r"Kandidat $m=5$: Misal $\sigma_5^B = (1\ 5)(2\ 4) \in C_{S_5}(\sigma_5^A)$",
            "pos": [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)],
            "col": PURE_RED
        },
        {
            "m": 4,
            "teks": r"Evaluasi $m=4$: Lolos superlevel untuk $\sigma_4^B = (1\ 4)(2\ 3) \in S_5$",
            "pos": [(0, 3), (1, 2), (2, 1), (3, 0), (4, 4)],
            "col": ORANGE
        },
        {
            "m": 3,
            "teks": r"Evaluasi $m=3$: Lolos syarat superlevel untuk $\sigma_3^B = (1\ 3)(4\ 5) \in S_5$",
            "pos": [(0, 2), (1, 1), (2, 0), (3, 4), (4, 3)],
            "col": TEAL
        },
        {
            "m": 2,
            "teks": r"Evaluasi $m=2$: Lolos syarat superlevel untuk $\sigma_2^B = (1\ 2)(3\ 5) \in S_5$",
            "pos": [(0, 1), (1, 0), (2, 4), (3, 3), (4, 2)],
            "col": PURE_BLUE
        },
        {
            "m": 1,
            "teks": r"Evaluasi $m=1$: Sisa entri otomatis membentuk permutasi $\sigma_1^B$.",
            "pos": [(0, 0), (1, 4), (2, 3), (3, 2), (4, 1)],
            "col": PURE_GREEN
        }
    ]
    
    prev_teks = None
    for step in tahapan:
        m = step["m"]
        v = 5 + m
        teks_mob = Tex(step["teks"], font_size=28, color=DARK_GRAY).next_to(judul_algo, DOWN, buff=0.2)
        
        if prev_teks:
            s.play(Transform(prev_teks, teks_mob))
        else:
            s.play(Write(teks_mob))
            prev_teks = teks_mob
            
        posisi = step["pos"]
        updates = []
        for r, c in posisi:
            B_vals[r][c] = m
            idx = r * 5 + c
            target_entry = b_star_mat.get_entries()[idx]
            new_entry = MathTex(str(m), font_size=28).set_color(step["col"]).move_to(target_entry)
            updates.append(Transform(target_entry, new_entry))
            
        boxes = VGroup(*[SurroundingRectangle(b_star_mat.get_entries()[r*5+c], color=step["col"], buff=0.05, stroke_opacity=0.5) for r,c in posisi])
        
        s.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.1), LaggedStart(*updates, lag_ratio=0.2), run_time=1)
        
        AB_res = get_max_plus_product(A_vals, B_vals)
        BA_res = get_max_plus_product(B_vals, A_vals)
        
        new_mat_AB = Matrix([[str(x) if x is not None else r"\varepsilon" for x in row] for row in AB_res], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(1).set_color(BLACK).move_to(mat_AB)
        for i, ent in enumerate(new_mat_AB.get_entries()):
            r, c = divmod(i, 5)
            ent.set_color(GRAY if AB_res[r][c] is None else BLACK)
                
        new_mat_BA = Matrix([[str(x) if x is not None else r"\varepsilon" for x in row] for row in BA_res], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(1).set_color(BLACK).move_to(mat_BA)
        for i, ent in enumerate(new_mat_BA.get_entries()):
            r, c = divmod(i, 5)
            ent.set_color(GRAY if BA_res[r][c] is None else BLACK)
                
        s.play(
            Transform(mat_AB, new_mat_AB),
            Transform(mat_BA, new_mat_BA),
            run_time=1
        )
        
        boxes_AB = VGroup()
        boxes_BA = VGroup()
        for i in range(5):
            for j in range(5):
                if AB_res[i][j] is not None and AB_res[i][j] >= v:
                    boxes_AB.add(SurroundingRectangle(new_mat_AB.get_entries()[i*5+j], color=step["col"], buff=0.05, stroke_opacity=0.5))
                if BA_res[i][j] is not None and BA_res[i][j] >= v:
                    boxes_BA.add(SurroundingRectangle(new_mat_BA.get_entries()[i*5+j], color=step["col"], buff=0.05, stroke_opacity=0.5))
                    
        s.play(Create(boxes_AB), Create(boxes_BA), run_time=0.8)
        s.wait(0.5)
        s.next_slide()
        s.play(FadeOut(boxes), FadeOut(boxes_AB), FadeOut(boxes_BA), run_time=0.2)
        
    teks_final = Tex(r"Seluruh entri matriks telah terisi valid, kandidat $B^*$ disimpan ke $\mathcal{P}(A)$.", font_size=32, color=PURPLE_E).to_edge(DOWN, buff=1.5)
    s.play(Write(teks_final))
    s.wait()
    s.next_slide()
    
    # BACKTRACKING DEMO
    teks_bt1 = Tex(r"Algoritma kemudian menelusuri mundur (\textit{backtrack}) untuk mencari solusi lain.", font_size=32, color=BLUE_E).to_edge(DOWN, buff=1.5)
    s.play(Transform(teks_final, teks_bt1))
    
    undo_anims = []
    for step_idx in [4, 3, 2, 1]:
        for r, c in tahapan[step_idx]["pos"]:
            B_vals[r][c] = None
            idx = r * 5 + c
            target_entry = b_star_mat.get_entries()[idx]
            new_entry = MathTex(r"\varepsilon", font_size=28).set_color(GRAY).move_to(target_entry)
            undo_anims.append(Transform(target_entry, new_entry))
        
    teks_bt2 = Tex(r"Mundur hingga ke $m=4$, lalu uji kandidat $\sigma_4^B$ yang lain.", font_size=30, color=BLACK).next_to(judul_algo, DOWN, buff=0.2)
    
    AB_res = get_max_plus_product(A_vals, B_vals)
    BA_res = get_max_plus_product(B_vals, A_vals)
    
    new_mat_AB = Matrix([[str(x) if x is not None else r"\varepsilon" for x in row] for row in AB_res], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(1).set_color(BLACK).move_to(mat_AB)
    for i, ent in enumerate(new_mat_AB.get_entries()):
        r, c = divmod(i, 5)
        ent.set_color(GRAY if AB_res[r][c] is None else BLACK)
        
    new_mat_BA = Matrix([[str(x) if x is not None else r"\varepsilon" for x in row] for row in BA_res], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(1).set_color(BLACK).move_to(mat_BA)
    for i, ent in enumerate(new_mat_BA.get_entries()):
        r, c = divmod(i, 5)
        ent.set_color(GRAY if BA_res[r][c] is None else BLACK)
        
    s.play(
        Transform(prev_teks, teks_bt2),
        LaggedStart(*undo_anims, lag_ratio=0.1),
        Transform(mat_AB, new_mat_AB),
        Transform(mat_BA, new_mat_BA),
        run_time=1.5
    )
    s.wait(1)
    s.next_slide()
    
    invalid_pos = [(0, 0), (1, 1), (2, 3), (3, 4), (4, 2)]
    teks_bt3 = Tex(r"Evaluasi $m=4$: Misal uji $\sigma_4^B = (3\ 4\ 5) \in S_5$", font_size=28, color=BLACK).next_to(judul_algo, DOWN, buff=0.2)
    s.play(Transform(prev_teks, teks_bt3))
    
    updates_inv = []
    for r, c in invalid_pos:
        B_vals[r][c] = 4
        idx = r * 5 + c
        target_entry = b_star_mat.get_entries()[idx]
        new_entry = MathTex("4", font_size=28).set_color(ORANGE).move_to(target_entry)
        updates_inv.append(Transform(target_entry, new_entry))
        
    boxes_inv = VGroup(*[SurroundingRectangle(b_star_mat.get_entries()[r*5+c], color=ORANGE, buff=0.05, stroke_opacity=0.5) for r,c in invalid_pos])
    s.play(LaggedStart(*[Create(b) for b in boxes_inv], lag_ratio=0.1), run_time=0.6)
    s.play(LaggedStart(*updates_inv, lag_ratio=0.2), run_time=1)
    
    AB_res = get_max_plus_product(A_vals, B_vals)
    BA_res = get_max_plus_product(B_vals, A_vals)
    
    new_mat_AB_inv = Matrix([[str(x) if x is not None else r"\varepsilon" for x in row] for row in AB_res], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(1).set_color(BLACK).move_to(mat_AB)
    for i, ent in enumerate(new_mat_AB_inv.get_entries()):
        r, c = divmod(i, 5)
        ent.set_color(GRAY if AB_res[r][c] is None else BLACK)
        
    new_mat_BA_inv = Matrix([[str(x) if x is not None else r"\varepsilon" for x in row] for row in BA_res], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(1).set_color(BLACK).move_to(mat_BA)
    for i, ent in enumerate(new_mat_BA_inv.get_entries()):
        r, c = divmod(i, 5)
        ent.set_color(GRAY if BA_res[r][c] is None else BLACK)
        
    s.play(
        Transform(mat_AB, new_mat_AB_inv),
        Transform(mat_BA, new_mat_BA_inv),
        run_time=1.2
    )
    
    boxes_AB_inv = VGroup()
    boxes_BA_inv = VGroup()
    v = 9
    for i in range(5):
        for j in range(5):
            if AB_res[i][j] is not None and AB_res[i][j] >= v:
                boxes_AB_inv.add(SurroundingRectangle(new_mat_AB_inv.get_entries()[i*5+j], color=ORANGE, buff=0.05, stroke_opacity=0.5))
            if BA_res[i][j] is not None and BA_res[i][j] >= v:
                boxes_BA_inv.add(SurroundingRectangle(new_mat_BA_inv.get_entries()[i*5+j], color=ORANGE, buff=0.05, stroke_opacity=0.5))
                
    s.play(Create(boxes_AB_inv), Create(boxes_BA_inv), run_time=0.8)
    s.wait(1)
    s.next_slide()
    
    diff_bg_AB = VGroup()
    diff_bg_BA = VGroup()
    for i in range(5):
        for j in range(5):
            cond_AB = (AB_res[i][j] is not None and AB_res[i][j] >= v)
            cond_BA = (BA_res[i][j] is not None and BA_res[i][j] >= v)
            if cond_AB and not cond_BA:
                bg_ab = SurroundingRectangle(new_mat_AB_inv.get_entries()[i*5+j], color=PURE_RED, fill_opacity=0.4, stroke_width=0, buff=0.12).set_z_index(-1)
                diff_bg_AB.add(bg_ab)
            elif cond_BA and not cond_AB:
                bg_ba = SurroundingRectangle(new_mat_BA_inv.get_entries()[i*5+j], color=PURE_RED, fill_opacity=0.4, stroke_width=0, buff=0.12).set_z_index(-1)
                diff_bg_BA.add(bg_ba)
                
    teks_bt4 = Tex(r"\mbox{Terlihat letak sel bernilai $\ge 9$ pada $AB^*$ berbeda dengan $B^*A$. Kandidat ditolak!}", font_size=28, color=PURE_RED).to_edge(DOWN, buff=1.5)
    s.play(
        Transform(teks_final, teks_bt4),
        FadeIn(diff_bg_AB), FadeIn(diff_bg_BA),
        run_time=1.5
    )
    s.wait(1)
    s.next_slide()
    
    teks_bt5 = Tex(r"Algoritma membatalkan penempatan dan lanjut menguji kandidat berikutnya.", font_size=30, color=BLACK).next_to(judul_algo, DOWN, buff=0.2)
    
    undo_inv_anims = []
    for r, c in invalid_pos:
        B_vals[r][c] = None
        idx = r * 5 + c
        target_entry = b_star_mat.get_entries()[idx]
        new_entry = MathTex(r"\varepsilon", font_size=28).set_color(GRAY).move_to(target_entry)
        undo_inv_anims.append(Transform(target_entry, new_entry))
        
    AB_res = get_max_plus_product(A_vals, B_vals)
    BA_res = get_max_plus_product(B_vals, A_vals)
    
    new_mat_AB_rest = Matrix([[str(x) if x is not None else r"\varepsilon" for x in row] for row in AB_res], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(1).set_color(BLACK).move_to(mat_AB)
    for i, ent in enumerate(new_mat_AB_rest.get_entries()):
        r, c = divmod(i, 5)
        ent.set_color(GRAY if AB_res[r][c] is None else BLACK)
        
    new_mat_BA_rest = Matrix([[str(x) if x is not None else r"\varepsilon" for x in row] for row in BA_res], v_buff=0.6, h_buff=0.6, element_alignment_corner=ORIGIN).scale(1).set_color(BLACK).move_to(mat_BA)
    for i, ent in enumerate(new_mat_BA_rest.get_entries()):
        r, c = divmod(i, 5)
        ent.set_color(GRAY if BA_res[r][c] is None else BLACK)
    
    s.play(
        Transform(prev_teks, teks_bt5),
        LaggedStart(*undo_inv_anims, lag_ratio=0.1),
        FadeOut(teks_final),
        Transform(mat_AB, new_mat_AB_rest),
        Transform(mat_BA, new_mat_BA_rest),
        FadeOut(boxes_inv), FadeOut(boxes_AB_inv), FadeOut(boxes_BA_inv),
        FadeOut(diff_bg_AB), FadeOut(diff_bg_BA),
        run_time=1
    )
    s.wait(1)
    s.next_slide()
    s.play(FadeOut(VGroup(grp_all, prev_teks, judul_algo), scale=0.5))

def TeoremaSuperlevel(s):
    Mobject.set_default(color=BLACK)
    judul = Title("Kriteria Komutatif Superlevel", color=BLACK, font_size=48, include_underline=True)
    judul[-1].set_color(BLACK)
    
    teorema = Tex(
        r"\parbox{" + str(config.frame_width) + r"cm}{"
        r"\textbf{Teorema 4.} Matriks $A, B \in L_S(n)$ saling komutatif ($A\otimes B = B\otimes A$) "
        r"$\iff \mathcal{U}_{\ge v}^{AB} = \mathcal{U}_{\ge v}^{BA} \quad \forall v \in \{n+2,\ldots,2n\}$.}",
        color=BLACK, font_size=30
    ).next_to(judul, DOWN, buff=0.4)
    
    s.play(Write(judul), Write(teorema))
    s.wait(1)
    s.next_slide()
    
    mat_C = Matrix([["8","7","6","7"],["7","8","7","6"],["6","7","8","7"],["7","6","7","8"]]).scale(0.5).set_color(BLACK)
    mat_D = Matrix([["8","7","6","7"],["7","8","7","6"],["6","7","8","7"],["7","6","7","8"]]).scale(0.5).set_color(BLACK)
    
    lbl_C = MathTex("A \otimes B =").scale(0.7).next_to(mat_C, LEFT)
    lbl_D = MathTex("B \otimes A =").scale(0.7).next_to(mat_D, LEFT)
    
    grp_C = VGroup(lbl_C, mat_C)
    grp_D = VGroup(lbl_D, mat_D)
    
    grp_CD = VGroup(grp_C, grp_D).arrange(RIGHT, buff=1.0).next_to(teorema, DOWN, buff=0.4)
    
    grid_AB = VGroup()
    grid_BA = VGroup()
    for i in range(4):
        for j in range(4):
            box1 = Square(side_length=0.3).set_stroke(color=DARK_GRAY, width=1)
            box2 = Square(side_length=0.3).set_stroke(color=DARK_GRAY, width=1)
            grid_AB.add(box1)
            grid_BA.add(box2)
            
    grid_AB.arrange_in_grid(rows=4, cols=4, buff=0).next_to(mat_C, DOWN, buff=0.5)
    grid_BA.arrange_in_grid(rows=4, cols=4, buff=0).next_to(mat_D, DOWN, buff=0.5)
    
    lbl_gAB = MathTex(r"\mathcal{U}_{\ge v}^{AB}").scale(0.6).next_to(grid_AB, DOWN, buff=0.1)
    lbl_gBA = MathTex(r"\mathcal{U}_{\ge v}^{BA}").scale(0.6).next_to(grid_BA, DOWN, buff=0.1)
    
    s.play(Create(grid_AB), Create(grid_BA), Write(lbl_gAB), Write(lbl_gBA), Write(grp_CD))
    s.wait(1)
    s.next_slide()
    
    levels = [(8, RED), (7, BLUE)]
    
    prev_hi_C = None
    prev_hi_D = None
    
    for v, col in levels:
        new_lbl_gAB = MathTex(r"\mathcal{U}_{\ge ", str(v), r"}^{AB}").scale(0.6).next_to(grid_AB, DOWN, buff=0.1)
        new_lbl_gAB[1].set_color(col)
        
        new_lbl_gBA = MathTex(r"\mathcal{U}_{\ge ", str(v), r"}^{BA}").scale(0.6).next_to(grid_BA, DOWN, buff=0.1)
        new_lbl_gBA[1].set_color(col)
        
        if prev_hi_C:
            s.play(
                Transform(lbl_gAB, new_lbl_gAB),
                Transform(lbl_gBA, new_lbl_gBA),
                FadeOut(prev_hi_C), FadeOut(prev_hi_D),
                *[f.animate.set_fill(opacity=0) for f in grid_AB],
                *[f.animate.set_fill(opacity=0) for f in grid_BA]
            )
        else:
            s.play(
                Transform(lbl_gAB, new_lbl_gAB),
                Transform(lbl_gBA, new_lbl_gBA)
            )
            
        highlights_C = VGroup()
        highlights_D = VGroup()
        fills_AB = VGroup()
        fills_BA = VGroup()
        
        mat_vals = [
            [8, 7, 6, 7],
            [7, 8, 7, 6],
            [6, 7, 8, 7],
            [7, 6, 7, 8]
        ]
        
        for i in range(4):
            for j in range(4):
                if mat_vals[i][j] >= v:
                    idx = i * 4 + j
                    highlights_C.add(SurroundingRectangle(mat_C.get_entries()[idx], color=col, buff=0.05))
                    highlights_D.add(SurroundingRectangle(mat_D.get_entries()[idx], color=col, buff=0.05))
                    fills_AB.add(grid_AB[idx])
                    fills_BA.add(grid_BA[idx])
                    
        s.play(Create(highlights_C), Create(highlights_D), run_time=0.8)
        s.play(
            LaggedStart(*[f.animate.set_fill(col, opacity=0.8) for f in fills_AB], lag_ratio=0.1),
            LaggedStart(*[f.animate.set_fill(col, opacity=0.8) for f in fills_BA], lag_ratio=0.1),
            run_time=1
        )
        
        s.wait(1)
        s.next_slide()
        
        prev_hi_C = highlights_C
        prev_hi_D = highlights_D
        
    concl_text = Tex(r"Elemen $n+1$ (yaitu $6$) pasti akan muncul dan posisinya pasti akan selalu sama.", font_size=32, color=PURPLE_E).to_edge(DOWN, buff=0.8)
    s.play(Write(concl_text))
    s.wait(1)
    s.next_slide()
    
    s.play(FadeOut(VGroup(judul, teorema, grp_CD, grid_AB, grid_BA, lbl_gAB, lbl_gBA, prev_hi_C, prev_hi_D, concl_text), shift=LEFT))

def HimpunanSuperlevel(s):
    Mobject.set_default(color=BLACK)
    judul = Title("Himpunan Superlevel", color=BLACK, font_size=48, include_underline=True)
    judul[-1].set_color(BLACK)
    
    deskripsi = Tex(
        r"\parbox{" + str(config.frame_width) + r"cm}{"
        r"\textbf{Definisi 5.} Himpunan superlevel dari hasil perkalian $A\otimes B$ pada level $v$, yang dinotasikan dengan $\mathcal{U}_{\ge v}^{AB}$, didefinisikan sebagai \[\mathcal{U}_{\ge v}^{AB}=\bigcup_{\substack{x,y\in \underline{n}\\x+y\ge v}}\Gamma(\sigma_y^B\circ\sigma_x^A).\]}", 
        color=BLACK, font_size=30).next_to(judul, DOWN, buff=0.2)
    s.play(Write(judul), Write(deskripsi), run_time=1)
    s.wait(1)
    s.next_slide()
    
    mat_A = Matrix([["1","2","3","4","5"],["2","1","4","5","3"],["3","5","1","2","4"],["4","3","5","1","2"],["5","4","2","3","1"]], v_buff=0.6, h_buff=0.8).scale(0.55).set_color(BLACK)
    mat_B = Matrix([["1","2","3","4","5"],["2","1","4","5","3"],["3","5","1","2","4"],["4","3","5","1","2"],["5","4","2","3","1"]], v_buff=0.6, h_buff=0.8).scale(0.55).set_color(BLACK)
    
    for ent in mat_A.get_entries(): ent.set_color(BLACK)
    for ent in mat_B.get_entries(): ent.set_color(BLACK)
    
    lbl_A = MathTex("A =").scale(0.7).next_to(mat_A, LEFT)
    lbl_B = MathTex("B =").scale(0.7).next_to(mat_B, LEFT)
    
    grp_A = VGroup(lbl_A, mat_A)
    grp_B = VGroup(lbl_B, mat_B)
    grp_matrices = VGroup(grp_A, grp_B).arrange(RIGHT, buff=1.0).next_to(deskripsi, DOWN, buff=0.5)
    
    s.play(Write(grp_matrices))
    s.wait(1)
    s.next_slide()


    s.play(grp_A.animate.to_edge(LEFT, buff=0.5).scale(0.6), grp_B.animate.to_edge(LEFT, buff=0.5).shift(DOWN*1.5).scale(0.6), run_time=1)
    
    mat_AB = Matrix([
        ["10", "9", "9", "8", "7"],
        ["9", "9", "10", "6", "8"],
        ["9", "8", "9", "10", "8"],
        ["8", "10", "7", "8", "9"],
        ["7", "7", "8", "9", "10"]
    ],element_alignment_corner=ORIGIN, v_buff=0.6, h_buff=0.8).scale(0.65).set_color(BLACK)
    for ent in mat_AB.get_entries(): ent.set_color(BLACK)
    lbl_AB = MathTex("A \otimes B =").scale(0.8).next_to(mat_AB, LEFT)
    grp_AB = VGroup(lbl_AB, mat_AB)
    
    grid = VGroup()
    for i in range(5):
        for j in range(5):
            box = Square(side_length=0.6).set_stroke(color=DARK_GRAY, width=1)
            lbl = MathTex(f"({i+1},{j+1})", font_size=16, color=DARK_GRAY).move_to(box)
            grid.add(VGroup(box, lbl))
    grid.arrange_in_grid(rows=5, cols=5, buff=0)
    grp_grid = grid
    
    grp_bottom = VGroup(grp_AB, grp_grid).arrange(RIGHT, buff=1.5).next_to(grp_matrices, RIGHT, buff=1)
    
    s.play(Write(grp_AB), Create(grid))
    s.wait(0.5)
    s.next_slide()
    
    levels = [
        (10, PURE_GREEN), 
        (9, TEAL), 
        (8, PURE_RED), 
        (7, ORANGE), 
        (6, PURE_BLUE)
    ]
    
    forms = {
        10: r"\mathcal{U}_{\ge 10}^{AB} &= \Gamma(\sigma_5^B \circ \sigma_5^A)",
        9: r"\mathcal{U}_{\ge 9}^{AB} &= \Gamma(\sigma_5^B \circ \sigma_5^A) \cup \Gamma(\sigma_4^B \circ \sigma_5^A) \cup \Gamma(\sigma_5^B \circ \sigma_4^A)",
        8: r"\mathcal{U}_{\ge 8}^{AB} &= \bigcup_{x+y \ge 8} \Gamma(\sigma_y^B \circ \sigma_x^A)",
        7: r"\mathcal{U}_{\ge 7}^{AB} &= \bigcup_{x+y \ge 7} \Gamma(\sigma_y^B \circ \sigma_x^A)",
        6: r"\mathcal{U}_{\ge 6}^{AB} &= \bigcup_{x+y \ge 6} \Gamma(\sigma_y^B \circ \sigma_x^A)"
    }
    
    prev_hi = None
    prev_form = None
    
    for v, col in levels:
        form_tex = MathTex(forms[v], font_size=28, color=col).to_edge(DOWN, buff=0.4)
        
        if prev_form:
            s.play(
                Transform(prev_form, form_tex),
                FadeOut(prev_hi),
                *[f[0].animate.set_fill(opacity=0) for f in grid]
            )
        else:
            s.play(Write(form_tex))
            prev_form = form_tex
            
        highlights = VGroup()
        fills = VGroup()
        
        mat_vals = [
            [10, 9, 9, 8, 7],
            [9, 9, 10, 6, 8],
            [9, 8, 9, 10, 8],
            [8, 10, 7, 8, 9],
            [7, 7, 8, 9, 10]
        ]
        
        for i in range(5):
            for j in range(5):
                if mat_vals[i][j] >= v:
                    idx = i * 5 + j
                    highlights.add(SurroundingRectangle(mat_AB[0][idx], color=col, buff=0.05))
                    fills.add(grid[idx][0])
                    
        s.play(Create(highlights),
            LaggedStart(*[f.animate.set_fill(col, opacity=0.8) for f in fills], lag_ratio=0.1),
            run_time=1
        )
        s.wait(1)
        s.next_slide()

        
        prev_hi = highlights
    
    s.play(FadeOut(VGroup(judul, deskripsi, grp_matrices, grp_AB, grid, prev_hi, prev_form), shift=LEFT), run_time=1)

def RepresentasiKoordinat(s):
    Mobject.set_default(color=BLACK)
    judul = Title("Representasi Koordinat", color=BLACK, font_size=48, include_underline=True)
    judul[-1].set_color(BLACK)
    
    deskripsi = Tex(
        r"\parbox{" + str(config.frame_width-1) + r"cm}{"
        r"\textbf{Definisi 4.} Representasi koordinat dari permutasi $\sigma$, dinotasikan $\Gamma(\sigma)$, didefinisikan sebagai himpunan pasangan nilai input dan outputnya. ($\Gamma(\sigma) = \{(r,\sigma(r))\mid r=1,\ldots,n\}$)}", 
        color=BLACK, font_size=32
    ).next_to(judul, DOWN, buff=0.5)
    
    s.play(Write(judul), Write(deskripsi), run_time=1)
    s.wait(0.5)
    s.next_slide()

    sigma_lbl = MathTex(r"\sigma =", font_size=40)
    cycle = VGroup(
        MathTex("(", font_size=40),
        MathTex("1", font_size=40),
        MathTex("4", font_size=40),
        MathTex("2", font_size=40),
        MathTex(")", font_size=40),
        MathTex("(", font_size=40),
        MathTex("3", font_size=40),
        MathTex("5", font_size=40),
        MathTex(")", font_size=40)
    ).arrange(RIGHT, buff=0.1)
    
    sigma_group = VGroup(sigma_lbl, cycle).arrange(RIGHT, buff=0.3).next_to(deskripsi, DOWN, buff=0.5).shift(LEFT*2)
    
    n = 5
    matrix_data = [[r"\varepsilon" for _ in range(n)] for _ in range(n)]
    mat_mobj = Matrix(matrix_data, v_buff=0.55, h_buff=0.55).scale(0.6).next_to(sigma_group, DOWN, buff=0.5)
    mat_mobj.set_color(BLACK)
    for ent in mat_mobj.get_entries(): ent.set_color(GRAY_C)
    
    row_labels = VGroup()
    col_labels = VGroup()
    for i in range(n):
        row_ref = mat_mobj.get_rows()[i]
        lbl_r = MathTex(str(i+1), color=BLUE_E, font_size=24)
        lbl_r.next_to(row_ref, RIGHT, buff=0.3)
        row_labels.add(lbl_r)
        col_ref = mat_mobj.get_columns()[i]
        lbl_c = MathTex(str(i+1), color=RED_E, font_size=24)
        lbl_c.next_to(col_ref, DOWN, buff=0.2)
        col_labels.add(lbl_c)
    
    mat_lbl = MathTex("P_\sigma =").scale(0.7).next_to(mat_mobj, LEFT)
    mat_group = VGroup(mat_lbl, mat_mobj, row_labels, col_labels).next_to(sigma_group, DOWN, buff=0.5)
    
    s.play(Write(mat_lbl), Create(mat_mobj), Write(row_labels), Write(col_labels), Write(sigma_group))
    
    gamma_text = MathTex(r"\Gamma(\sigma)", font_size=32).next_to(sigma_group, RIGHT, buff=2.0)

    s.play(Write(gamma_text))
    s.next_slide(loop=True)
    
    coords = VGroup()
    entries = mat_mobj.get_entries()
    last_coord = None

    mappings = [
        (1, 4, cycle[1], cycle[2]), 
        (4, 2, cycle[2], cycle[3]), 
        (2, 1, cycle[3], cycle[1]),
        (3, 5, cycle[6], cycle[7]),
        (5, 3, cycle[7], cycle[6])
    ]
    
    for i, (r, c, mob_in, mob_out) in enumerate(mappings):
        s.play(
            mob_in.animate.set_color(BLUE).scale(1.2), 
            mob_out.animate.set_color(RED).scale(1.2),  
            row_labels[r-1].animate.set_color(BLUE).set_weight(BOLD).scale(1.2),
            col_labels[c-1].animate.set_color(RED).set_weight(BOLD).scale(1.2),
            run_time=0.2
        )
        
        coord_tex = MathTex("(", str(r), ",", str(c), ")", font_size=32)
        coord_tex[1].set_color(BLUE_E)
        coord_tex[3].set_color(RED_E)
        
        if last_coord is None:
            coord_tex.next_to(gamma_text, DOWN, buff=0.3)
        else:
            coord_tex.next_to(last_coord, DOWN, buff=0.2).align_to(last_coord, LEFT)
        
        idx = (r-1)*n + (c-1)
        target_entry = entries[idx]
        new_val = MathTex("0", color=BLACK, font_size=28).move_to(target_entry)
        
        sr_target = SurroundingRectangle(target_entry, color=PURPLE, buff=0.1)
        
        s.play(
            TransformFromCopy(VGroup(mob_in, mob_out), coord_tex),
            Transform(target_entry, new_val),
            Create(sr_target),
            run_time=0.4
        )
        s.play(FadeOut(sr_target), run_time=0.2)
            
        coords.add(coord_tex)
        last_coord = coord_tex
        
        s.play(
            mob_in.animate.set_color(BLACK).scale(1/1.2),
            mob_out.animate.set_color(BLACK).scale(1/1.2),
            row_labels[r-1].animate.set_color(BLUE_E).set_weight(NORMAL).scale(1/1.2),
            col_labels[c-1].animate.set_color(RED_E).set_weight(NORMAL).scale(1/1.2),
            run_time=0.4
        )

    gamma_box = SurroundingRectangle(VGroup(gamma_text, coords), color=PURPLE_E, buff=0.2)
    s.play(Create(gamma_box))
    s.wait(1)
    s.next_slide()
    
    s.play(FadeOut(VGroup(judul, deskripsi, sigma_group, mat_group, gamma_text, coords, gamma_box), shift=LEFT), run_time=1)

def SyaratCukup(s):
    s.next_slide()
    Mobject.set_default(color=BLACK)
    judul = Title("Syarat Cukup Latin Square Komutatif", color=BLACK, font_size=48, include_underline=True)
    judul[-1].set_color(BLACK)
    
    teorema = Tex(
        r"\parbox{" + str(config.frame_width) + r"cm}{"
        r"\textbf{Teorema 5.} Misalkan $A,B\in L_S(n)$ dengan dekomposisi $A=\bigoplus_{i=1}^{n} i\otimes P_{\sigma_i^A}$ dan $B=\bigoplus_{j=1}^{n} j\otimes P_{\sigma_j^B}$. Jika terdapat subgrup abelian $H\le S_n$ sedemikian sehingga $\sigma_i^A\in H$ dan $\sigma_j^B\in H$ untuk setiap $i,j\in \underline{n}$, maka ",r"$A\otimes B=B\otimes A$.}",
        color=BLACK, font_size=30
    ).next_to(judul, DOWN, buff=0.4)
    s.play(Write(judul),Write(teorema), run_time=1)
    s.wait(1)
    s.next_slide()
    
    text_pos = teorema.get_bottom() + DOWN * 0.5
    eq_pos = text_pos + DOWN * 0.8
    
    dek_teks = Tex(r"*Tinjau perkalian dekomposisi $A$ dan $B$:", color=DARK_GRAY, font_size=30).move_to(text_pos)
    
    eq_ab = MathTex(
        "A", r"\otimes", "B", r"=", 
        r"\left( \bigoplus_{i=1}^n ", "i", r"\otimes", "P_{\sigma_i^A}", r" \right)", 
        r"\otimes", 
        r"\left( \bigoplus_{j=1}^n ", "j", r"\otimes", "P_{\sigma_j^B}", r" \right)",
        color=BLACK, font_size=32
    ).move_to(eq_pos)
    eq_ab[0].set_color(PURE_BLUE)
    eq_ab[2].set_color(PURE_RED)
    eq_ab[5].set_color(PURE_BLUE)
    eq_ab[7].set_color(PURE_BLUE)
    eq_ab[11].set_color(PURE_RED)
    eq_ab[13].set_color(PURE_RED)
    
    s.play(Write(eq_ab),Write(dek_teks))
    s.wait(1)
    s.next_slide()
    
    dist_teks = Tex(r"*Distribusikan perkalian max-plus:", color=DARK_GRAY, font_size=30).move_to(text_pos)
    
    eq_dist = MathTex(
        "A", r"\otimes", "B", r"=",
        r"\bigoplus_{i=1}^n \bigoplus_{j=1}^n (", "i", "+", "j", r") \otimes (", "P_{\sigma_i^A}", r"\otimes", "P_{\sigma_j^B}", ")",
        color=BLACK, font_size=32
    ).move_to(eq_pos)
    eq_dist[0].set_color(PURE_BLUE)
    eq_dist[2].set_color(PURE_RED)
    eq_dist[5].set_color(PURE_BLUE)
    eq_dist[7].set_color(PURE_RED)
    eq_dist[9].set_color(PURE_BLUE)
    eq_dist[11].set_color(PURE_RED)
    
    s.play(
        ReplacementTransform(dek_teks, dist_teks),
        ReplacementTransform(eq_ab, eq_dist)
    )
    s.wait(1)
    s.next_slide()
    
    kom_teks = Tex(r"*Karena $H$ abelian, $\sigma_i^A$ dan $\sigma_j^B$ komutatif, sehingga:", color=DARK_GRAY, font_size=30).move_to(text_pos)
    
    eq_kom = MathTex(
        "A", r"\otimes", "B", r"=",
        r"\bigoplus_{i=1}^n \bigoplus_{j=1}^n (", "i", "+", "j", r") \otimes (", "P_{\sigma_j^B}", r"\otimes", "P_{\sigma_i^A}", ")",
        color=BLACK, font_size=32
    ).move_to(eq_pos)
    eq_kom[0].set_color(PURE_BLUE)
    eq_kom[2].set_color(PURE_RED)
    eq_kom[5].set_color(PURE_BLUE)
    eq_kom[7].set_color(PURE_RED)
    eq_kom[9].set_color(PURE_RED)
    eq_kom[11].set_color(PURE_BLUE)
    
    s.play(
        ReplacementTransform(dist_teks, kom_teks),
        ReplacementTransform(eq_dist, eq_kom)
    )
    s.wait(1)
    s.next_slide()
    
    rev_teks = Tex(r"*Kembalikan bentuk distribusi menjadi perkalian dua dekomposisi:", color=DARK_GRAY, font_size=30).move_to(text_pos)
    
    eq_rev = MathTex(
        "A", r"\otimes", "B", r"=", 
        r"\left( \bigoplus_{j=1}^n ", "j", r"\otimes", "P_{\sigma_j^B}", r" \right)", 
        r"\otimes", 
        r"\left( \bigoplus_{i=1}^n ", "i", r"\otimes", "P_{\sigma_i^A}", r" \right)",
        color=BLACK, font_size=32
    ).move_to(eq_pos)
    eq_rev[0].set_color(PURE_BLUE)
    eq_rev[2].set_color(PURE_RED)
    eq_rev[5].set_color(PURE_RED)
    eq_rev[7].set_color(PURE_RED)
    eq_rev[11].set_color(PURE_BLUE)
    eq_rev[13].set_color(PURE_BLUE)
    
    s.play(
        ReplacementTransform(kom_teks, rev_teks),
        ReplacementTransform(eq_kom, eq_rev)
    )
    s.wait(1)
    s.next_slide()
    
    final_teks = Tex(r"*Yang tidak lain adalah definisi dekomposisi untuk $B \otimes A$:", color=DARK_GRAY, font_size=30).move_to(text_pos)
    
    eq_final = MathTex(
        "A", r"\otimes", "B", "=", "B", r"\otimes", "A",
        color=BLACK, font_size=32
    ).move_to(eq_pos)
    eq_final[0].set_color(PURE_BLUE)
    eq_final[2].set_color(PURE_RED)
    eq_final[4].set_color(PURE_RED)
    eq_final[6].set_color(PURE_BLUE)
    
    s.play(
        ReplacementTransform(rev_teks, final_teks),
        ReplacementTransform(eq_rev, eq_final)
    )
    
    box_teo = SurroundingRectangle(teorema[1], color=PURPLE_E)
    s.play(
        ReplacementTransform(eq_final, teorema[1]),
        teorema[1][0].animate.set_color(PURE_BLUE),
        teorema[1][2].animate.set_color(PURE_RED),
        teorema[1][4].animate.set_color(PURE_RED),
        teorema[1][6].animate.set_color(PURE_BLUE),
        FadeOut(final_teks)
    )
    s.play(Indicate(box_teo, color=PURPLE_E), run_time=0.5)
    s.wait(1)
    s.next_slide()
    
    s.play(FadeOut(box_teo))
    
    akibat = Tex(
        r"\parbox{" + str(config.frame_width) + r"cm}{"
        r"\textbf{Akibat 2.} Misalkan $A,B\in L_S(n)$ adalah Latin square sirkulan, maka",r" $A\otimes B=B\otimes A$",r" (komutatif).}",
        color=BLACK, font_size=30
    ).next_to(teorema, DOWN, buff=0.8)
    
    s.play(Write(akibat))
    s.wait(1)
    s.next_slide()
    
    text_pos2 = akibat.get_bottom() + DOWN * 0.5
    eq_pos2 = text_pos2 + DOWN * 0.8
    
    bukti_akibat_title = Tex(r"*Karena $A$ dan $B$ sirkulan, permutasinya dibangkitkan oleh sikel", color=DARK_GRAY, font_size=30).move_to(text_pos2)
    
    eq_siklus = MathTex(
        r"H = \langle (1\ 2\ \dots\ n) \rangle",
        color=BLACK, font_size=32
    ).move_to(eq_pos2)
    s.play(Write(bukti_akibat_title), Write(eq_siklus))
    s.wait(1)
    s.next_slide()
    
    abelian_teks = Tex(r"*Setiap subgrup siklik pasti merupakan subgrup abelian, sehingga:", color=DARK_GRAY, font_size=30).move_to(text_pos2)
    
    eq_abelian = MathTex(
        r"H \text{ adalah subgrup abelian dari } S_n",
        color=BLACK, font_size=32
    ).move_to(eq_pos2)
    
    s.play(
        ReplacementTransform(bukti_akibat_title, abelian_teks),
        ReplacementTransform(eq_siklus, eq_abelian)
    )
    s.wait(1)
    s.next_slide()
    
    syarat_teks = Tex(r"*Berdasarkan \textbf{Teorema 5}, karena syarat subgrup abelian terpenuhi, maka:", color=DARK_GRAY, font_size=30).move_to(text_pos2)
    
    eq_akhir = MathTex(
        "A", r"\otimes", "B", "=", "B", r"\otimes", "A",
        color=BLACK, font_size=32
    ).move_to(eq_pos2)
    eq_akhir[0].set_color(PURE_BLUE)
    eq_akhir[2].set_color(PURE_RED)
    eq_akhir[4].set_color(PURE_RED)
    eq_akhir[6].set_color(PURE_BLUE)
    
    s.play(
        ReplacementTransform(abelian_teks, syarat_teks),
        ReplacementTransform(eq_abelian, eq_akhir)
    )
    s.wait(1)
    s.next_slide()
    
    box_akibat = SurroundingRectangle(akibat[1], color=PURPLE_E)
    s.play(
        ReplacementTransform(eq_akhir, akibat[1]),
        akibat[1][0].animate.set_color(PURE_BLUE),
        akibat[1][2].animate.set_color(PURE_RED),
        akibat[1][4].animate.set_color(PURE_RED),
        akibat[1][6].animate.set_color(PURE_BLUE),
        FadeOut(syarat_teks)
    )
    s.play(Indicate(box_akibat, color=PURPLE_E), run_time=0.5)
    s.wait(0.5)
    s.play(Uncreate(box_akibat))
    s.next_slide()

    
    s.play(FadeOut(VGroup(box_akibat, akibat, teorema, judul), shift=LEFT))

def SyaratPerlu(s):
    s.next_slide()
    Mobject.set_default(color=BLACK)
    judul = Title("Syarat Perlu Latin Square Komutatif", color=BLACK, font_size=48, include_underline=True)
    judul[-1].set_color(BLACK)
    
    deskripsi = Tex(
        r"\parbox{" + str(config.frame_width) + r"cm}{"
        r"\textbf{Akibat 1.} Misalkan $A,B\in L_S(n)$ dan misalkan $P_\rho$ adalah matriks permutasi max-plus yang bersesuaian dengan permutasi $\rho\in S_n$. Jika $A\otimes B=B\otimes A$, maka}",
        color=BLACK, font_size=30
    ).next_to(judul, DOWN, buff=0.4)
    
    s.play(Write(deskripsi),Write(judul), run_time=1)
    s.wait(1)
    s.next_slide()

    full_eq = MathTex(
        r"(", r"P_\rho^{-1}", r"\otimes", "A", r"\otimes", r"P_\rho", r")",
        r"\otimes",
        r"(", r"P_\rho^{-1}", r"\otimes", "B", r"\otimes", r"P_\rho", r")",
        "=",
        r"(", r"P_\rho^{-1}", r"\otimes", "B", r"\otimes", r"P_\rho", r")",
        r"\otimes",
        r"(", r"P_\rho^{-1}", r"\otimes", "A", r"\otimes", r"P_\rho", r")",
        font_size=32
    ).next_to(deskripsi, DOWN, buff=0.4)
    full_eq[3].set_color(PURE_BLUE)
    full_eq[11].set_color(PURE_RED)
    full_eq[19].set_color(PURE_RED)
    full_eq[27].set_color(PURE_BLUE)

    s.play(Write(full_eq), run_time=0.75)
    s.wait(1)
    s.next_slide(auto_next=True)

    eq1 = MathTex(
        r"(", r"P_\rho^{-1}", r"\otimes", "A", r"\otimes", r"P_\rho", r")",
        r"\otimes",
        r"(", r"P_\rho^{-1}", r"\otimes", "B", r"\otimes", r"P_\rho", r")",
        font_size=42
    )
    eq1[3].set_color(PURE_BLUE)
    eq1[11].set_color(PURE_RED)
    eq1.next_to(full_eq, DOWN, buff=0.8)
    
    s.play(ReplacementTransform(full_eq[0:15].copy(), eq1), run_time=0.75)

    eq2 = MathTex(
        r"P_\rho^{-1}", r"\otimes", "A", r"\otimes", r"P_\rho",
        r"\otimes",
        r"P_\rho^{-1}", r"\otimes", "B", r"\otimes", r"P_\rho",
        font_size=42
    )
    eq2[2].set_color(PURE_BLUE)
    eq2[8].set_color(PURE_RED)
    eq2.move_to(eq1)

    s.play(
        FadeOut(eq1[0], shift=UP), FadeOut(eq1[6], shift=UP),
        FadeOut(eq1[8], shift=UP), FadeOut(eq1[14], shift=UP),
        ReplacementTransform(eq1[1], eq2[0]),
        ReplacementTransform(eq1[2], eq2[1]),
        ReplacementTransform(eq1[3], eq2[2]),
        ReplacementTransform(eq1[4], eq2[3]),
        ReplacementTransform(eq1[5], eq2[4]),
        ReplacementTransform(eq1[7], eq2[5]),
        ReplacementTransform(eq1[9], eq2[6]),
        ReplacementTransform(eq1[10], eq2[7]),
        ReplacementTransform(eq1[11], eq2[8]),
        ReplacementTransform(eq1[12], eq2[9]),
        ReplacementTransform(eq1[13], eq2[10])
    )
    s.wait(0.5)
    s.next_slide(auto_next=True)

    box = SurroundingRectangle(eq2[4:7], color=GREEN_E, buff=0.1)
    s.play(Create(box))
    ident = MathTex("I", color=GREEN_E, font_size=42).move_to(box)
    s.play(ReplacementTransform(eq2[4:7], ident), FadeOut(box))
    s.wait(0.5)
    s.next_slide(auto_next=True)

    eq3 = MathTex(r"P_\rho^{-1}", r"\otimes", "A", r"\otimes", "B", r"\otimes", r"P_\rho", font_size=42)
    eq3[2].set_color(PURE_BLUE)
    eq3[4].set_color(PURE_RED)
    eq3.move_to(eq2)

    s.play(
        FadeOut(ident, scale=0),
        FadeOut(eq2[7]),
        ReplacementTransform(eq2[0:3], eq3[0:3]),
        ReplacementTransform(eq2[3], eq3[3]),
        ReplacementTransform(eq2[8:11], eq3[4:7])
    )
    s.wait(0.5)
    s.next_slide(auto_next=True)


    box2 = SurroundingRectangle(eq3[2:5], color=DARK_GRAY, buff=0.1)
    s.play(Create(box2))
    
    asumsi_popup = MathTex("A", r"\otimes", "B", "=", "B", r"\otimes", "A", color=BLACK, font_size=36)
    asumsi_popup[0].set_color(PURE_BLUE)
    asumsi_popup[2].set_color(PURE_RED)
    asumsi_popup[4].set_color(PURE_RED)
    asumsi_popup[6].set_color(PURE_BLUE)
    asumsi_popup.next_to(box2, DOWN, buff=0.3)
    
    s.play(FadeIn(asumsi_popup, shift=UP))
    s.wait(0.5)
    s.next_slide(auto_next=True)
    
    eq4 = MathTex(r"P_\rho^{-1}", r"\otimes", "B", r"\otimes", "A", r"\otimes", r"P_\rho", font_size=42)
    eq4[2].set_color(PURE_RED)
    eq4[4].set_color(PURE_BLUE)
    eq4.move_to(eq3)

    s.play(
        eq3[2].animate(path_arc=PI/2).move_to(eq4[4]),
        eq3[4].animate(path_arc=PI/2).move_to(eq4[2]),
        eq3[0:2].animate.move_to(eq4[0:2]),
        eq3[3].animate.move_to(eq4[3]),
        eq3[5:7].animate.move_to(eq4[5:7]),
        run_time=0.75
    )
    s.remove(*eq3)
    s.add(eq4)
    s.wait(0.5)
    s.next_slide(auto_next=True)
    s.play(FadeOut(box2), FadeOut(asumsi_popup, shift=DOWN))

    ident2 = MathTex("I", color=GREEN_E, font_size=42).move_to(eq4[3])
    s.play(
        eq4[0:3].animate.shift(LEFT*1.2),
        eq4[4:7].animate.shift(RIGHT*1.2),
        ReplacementTransform(eq4[3], ident2)
    )
    s.wait(0.5)
    s.next_slide(auto_next=True)

    eq5 = MathTex(
        r"P_\rho^{-1}", r"\otimes", "B", r"\otimes", r"P_\rho",
        r"\otimes",
        r"P_\rho^{-1}", r"\otimes", "A", r"\otimes", r"P_\rho",
        font_size=42
    )
    eq5[2].set_color(PURE_RED)
    eq5[8].set_color(PURE_BLUE)
    eq5.move_to(eq1)

    s.play(
        ReplacementTransform(ident2, eq5[4:7]),
        ReplacementTransform(eq4[0:3], eq5[0:3]),
        ReplacementTransform(eq4[3], eq5[3]),
        FadeIn(eq5[7]),
        ReplacementTransform(eq4[4:7], eq5[8:11])
    )
    s.wait(0.5)
    s.next_slide(auto_next=True)

    eq6 = MathTex(
        r"(", r"P_\rho^{-1}", r"\otimes", "B", r"\otimes", r"P_\rho", r")",
        r"\otimes",
        r"(", r"P_\rho^{-1}", r"\otimes", "A", r"\otimes", r"P_\rho", r")",
        font_size=42
    )
    eq6[3].set_color(PURE_RED)
    eq6[11].set_color(PURE_BLUE)
    eq6.move_to(eq5)

    s.play(
        ReplacementTransform(eq5[0:5], eq6[1:6]),
        ReplacementTransform(eq5[5], eq6[7]),
        ReplacementTransform(eq5[6:11], eq6[9:14]),
        FadeIn(eq6[0], shift=DOWN), FadeIn(eq6[6], shift=DOWN),
        FadeIn(eq6[8], shift=DOWN), FadeIn(eq6[14], shift=DOWN)
    )
    s.wait(0.5)
    s.next_slide()

    s.play(
        eq6.animate.scale(32/42).move_to(full_eq[16:31]),
        run_time=0.75
    )
    box_rhs = SurroundingRectangle(full_eq, color=BLACK, buff=0.1)
    s.play(Write(box_rhs),FadeOut(eq6))
    s.wait(1)
    s.next_slide()

    teorema = Tex(
        r"\parbox{" + str(config.frame_width) + r"cm}{"
        r"\textbf{Teorema 4.} Misalkan $A, B \in L_S(n)$ dengan himpunan simbol $\underline{n}$. Jika matriks $A$ dan $B$ saling komutatif terhadap perkalian max-plus, yaitu $A \otimes B = B \otimes A$, maka permutasi yang bersesuaian dengan simbol maksimum $n$ dari kedua matriks tersebut saling komutatif, yaitu:}",
        color=BLACK, font_size=30
    ).next_to(full_eq, DOWN, buff=0.4)
    
    eq_teo = MathTex(r"\sigma_n^A", r"\circ", r"\sigma_n^B", r"=", r"\sigma_n^B", r"\circ", r"\sigma_n^A", color=BLACK, font_size=36)
    eq_teo.next_to(teorema, DOWN, buff=0.3)
    
    s.play(Write(eq_teo), Write(teorema))
    s.wait(1)
    s.next_slide()
    
    text_pos = eq_teo.get_bottom() + DOWN * 0.5
    eq_pos = text_pos + DOWN * 0.8
    
    dek_teks = Tex(r"*Tinjau dekomposisi Latin square untuk $A$ dan $B$:", color=DARK_GRAY, font_size=30).move_to(text_pos)
    s.play(Write(dek_teks))
    
    dek_A = MathTex(r"A", r"=", r"\bigoplus_{k=1}^n (k \otimes P_k^A)", color=BLACK, font_size=32)
    dek_B = MathTex(r"B", r"=", r"\bigoplus_{k=1}^n (k \otimes P_k^B)", color=BLACK, font_size=32)
    dek_A[0].set_color(PURE_BLUE)
    dek_B[0].set_color(PURE_RED)
    dek_group = VGroup(dek_A, dek_B).arrange(RIGHT, buff=0.5).move_to(eq_pos)
    s.play(Write(dek_group))
    s.wait(1)
    s.next_slide()
    
    subst_teks = Tex(r"*Substitusi ke asumsi $A \otimes B = B \otimes A$:", color=DARK_GRAY, font_size=30).move_to(text_pos)
    
    eq_subst = MathTex(
        r"\left( \bigoplus_{i=1}^n (i \otimes P_i^A) \right)", r"\otimes", r"\left( \bigoplus_{j=1}^n (j \otimes P_j^B) \right)",
        r"=",
        r"\left( \bigoplus_{i=1}^n (i \otimes P_i^B) \right)", r"\otimes", r"\left( \bigoplus_{j=1}^n (j \otimes P_j^A) \right)",
        color=BLACK, font_size=32
    ).move_to(eq_pos)
    eq_subst[0].set_color(PURE_BLUE)
    eq_subst[2].set_color(PURE_RED)
    eq_subst[4].set_color(PURE_RED)
    eq_subst[6].set_color(PURE_BLUE)
    
    s.play(
        FadeOut(dek_teks),
        FadeIn(subst_teks),
        ReplacementTransform(dek_group, eq_subst)
    )
    s.wait(1)
    s.next_slide()
    
    kalimat_2n = Tex(r"*Karena nilai maksimum $2n$ pasti muncul dari $n \otimes n$, maka:", color=DARK_GRAY, font_size=30).move_to(text_pos)
    
    eq_2n = MathTex(
        r"(n \otimes P_n^A)", r"\otimes", r"(n \otimes P_n^B)",
        r"=",
        r"(n \otimes P_n^B)", r"\otimes", r"(n \otimes P_n^A)",
        color=BLACK, font_size=32
    ).move_to(eq_pos)
    eq_2n[0].set_color(PURE_BLUE)
    eq_2n[2].set_color(PURE_RED)
    eq_2n[4].set_color(PURE_RED)
    eq_2n[6].set_color(PURE_BLUE)
    
    s.play(
        FadeOut(subst_teks),
        FadeIn(kalimat_2n),
        ReplacementTransform(eq_subst, eq_2n)
    )
    s.wait(1)
    s.next_slide()
    
    kalimat_komutatif = Tex(r"*Sehingga matriks permutasinya pun harus komutatif:", color=DARK_GRAY, font_size=30).move_to(text_pos)
    
    eq_P = MathTex(r"P_n^A", r"\otimes", r"P_n^B", r"=", r"P_n^B", r"\otimes", r"P_n^A", color=BLACK, font_size=36).move_to(eq_pos)
    eq_P[0].set_color(PURE_BLUE)
    eq_P[2].set_color(PURE_RED)
    eq_P[4].set_color(PURE_RED)
    eq_P[6].set_color(PURE_BLUE)
    
    s.play(
        FadeOut(kalimat_2n),
        FadeIn(kalimat_komutatif),
        ReplacementTransform(eq_2n, eq_P)
    )
    s.wait(1)
    s.next_slide()
    
    kalimat_final = Tex(r"*Akibatnya, permutasinya juga saling komutatif:", color=DARK_GRAY, font_size=30).move_to(text_pos)
    
    eq_final = MathTex(r"\sigma_n^A", r"\circ", r"\sigma_n^B", r"=", r"\sigma_n^B", r"\circ", r"\sigma_n^A", color=BLACK, font_size=36).move_to(eq_pos)
    eq_final[0].set_color(PURE_BLUE)
    eq_final[2].set_color(PURE_RED)
    eq_final[4].set_color(PURE_RED)
    eq_final[6].set_color(PURE_BLUE)
    
    s.play(
        FadeOut(kalimat_komutatif),
        FadeIn(kalimat_final),
        ReplacementTransform(eq_P, eq_final)
    )
    s.play(Transform(eq_final, eq_teo))
    eq_teo[0].set_color(PURE_BLUE)
    eq_teo[2].set_color(PURE_RED)
    eq_teo[4].set_color(PURE_RED)
    eq_teo[6].set_color(PURE_BLUE)

    final_box_teo = SurroundingRectangle(eq_teo, color=PURPLE_E, buff=0.2)
    s.play(Create(final_box_teo))
    s.wait(1)
    s.next_slide()
    s.play(Uncreate(final_box_teo))
    s.play(FadeOut(VGroup(full_eq,box_rhs,deskripsi,judul),shift=LEFT), FadeOut(VGroup(teorema,eq_teo,final_box_teo,kalimat_final,eq_final),shift=LEFT))

def InvariansiLatinSquare(s):
    judul = Title("Invariansi Latin Square", color=BLACK, font_size=48, include_underline=True)
    judul[-1].set_color(BLACK)
    teorema_tex = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Misalkan $A\in L_S(n)$ dan misalkan $P_\sigma$, $P_\tau$ adalah matriks permutasi max-plus yang bersesuaian dengan permutasi $\sigma,\tau\in S_n$. Maka $P_\sigma\otimes A$, $A\otimes P_\tau$, dan $P_\sigma\otimes A\otimes P_\tau$ juga merupakan \textit{Latin square}.""", color=BLACK, font_size=30)
    teorema_tex.next_to(judul, DOWN, buff=0.3)
    s.play(Write(judul), Write(teorema_tex), run_time=0.75)
    s.wait(1)
    s.next_slide()
    teks_kiri = MathTex(r"\text{Perkalian Kiri: } P_\sigma \otimes A \implies \text{Permutasi Baris}", color=DARK_GRAY, font_size=32)
    teks_kiri.next_to(teorema_tex, DOWN, buff=0.8)
    mat_P = Matrix([
        [r"\varepsilon", "0", r"\varepsilon"],
        ["0", r"\varepsilon", r"\varepsilon"],
        [r"\varepsilon", r"\varepsilon", "0"]
    ], v_buff=0.8, h_buff=0.8).set_color(BLACK)
    mat_P_label = MathTex("P_\sigma", color=BLACK).next_to(mat_P, DOWN, buff=0.3)
    group_P = VGroup(mat_P, mat_P_label)
    mat_A = Matrix([
        ["1", "2", "3"],
        ["2", "3", "1"],
        ["3", "1", "2"]
    ], v_buff=0.8, h_buff=0.8).set_color(BLACK)
    mat_A_label = MathTex("A", color=BLACK).next_to(mat_A, DOWN, buff=0.3)
    group_A = VGroup(mat_A, mat_A_label)
    mat_Res1 = Matrix([
        ["2", "3", "1"],
        ["1", "2", "3"],
        ["3", "1", "2"]
    ], v_buff=0.8, h_buff=0.8).set_color(BLACK)
    op_times1 = MathTex(r"\otimes", color=BLACK)
    op_eq1 = MathTex("=", color=BLACK)
    eq_kiri = VGroup(group_P, op_times1, group_A, op_eq1, mat_Res1).arrange(RIGHT, buff=0.5).next_to(teks_kiri, DOWN, buff=0.1).scale(0.7)
    op_times1.shift(UP*0.25)
    op_eq1.shift(UP*0.25)
    mat_Res1.shift(UP*0.25)

    s.play(Write(teks_kiri), Write(group_P), Write(op_times1), Write(group_A), Write(op_eq1), run_time=0.75)
    s.wait()
    s.next_slide()
    rows_A = mat_A.get_rows()
    rows_Res1 = mat_Res1.get_rows()
    box_P_r1 = SurroundingRectangle(mat_P.get_rows()[0], color=ORANGE, buff=0.1)
    box_P_0_1 = SurroundingRectangle(mat_P.get_entries()[1], color=RED_E, buff=0.05)

    row_copy_2 = rows_A[1].copy()
    s.play(Create(box_P_r1), Create(box_P_0_1),row_copy_2.animate.set_color(RED_E), run_time=0.8)
    s.play(Transform(row_copy_2, rows_Res1[0].copy().set_color(RED_E)), run_time=0.3)
    box_P_r2 = SurroundingRectangle(mat_P.get_rows()[1], color=ORANGE, buff=0.1)
    box_P_0_2 = SurroundingRectangle(mat_P.get_entries()[3], color=BLUE_E, buff=0.05)

    row_copy_1 = rows_A[0].copy()
    s.play(
        Transform(box_P_r1, box_P_r2),
        Transform(box_P_0_1, box_P_0_2),
        row_copy_1.animate.set_color(BLUE_E),
        run_time=0.5
    )
    
    s.play(Transform(row_copy_1, rows_Res1[1].copy().set_color(BLUE_E)), run_time=0.3)
    box_P_r3 = SurroundingRectangle(mat_P.get_rows()[2], color=ORANGE, buff=0.1)
    box_P_0_3 = SurroundingRectangle(mat_P.get_entries()[8], color=GREEN_E, buff=0.05)

    row_copy_3 = rows_A[2].copy()
    s.play(
        Transform(box_P_r1, box_P_r3),
        Transform(box_P_0_1, box_P_0_3),
        row_copy_3.animate.set_color(GREEN_E),
        run_time=0.5
    )

    s.play(Transform(row_copy_3, rows_Res1[2].copy().set_color(GREEN_E)), run_time=0.3)
    s.wait(1)
    s.play(
        FadeOut(box_P_r1), FadeOut(box_P_0_1),
        row_copy_1.animate.set_color(BLACK),
        row_copy_2.animate.set_color(BLACK),
        row_copy_3.animate.set_color(BLACK),
        run_time=0.5
    )
    mat_Res1_final = mat_Res1.copy()
    s.add(mat_Res1_final)
    s.remove(row_copy_1, row_copy_2, row_copy_3)
    box_LS1 = SurroundingRectangle(mat_Res1_final, color=PURPLE_E, buff=0.2)
    teks_LS1 = MathTex(r"\in L_S(n)", color=PURPLE_E).next_to(box_LS1, DOWN)
    s.play(Create(box_LS1), Write(teks_LS1))
    s.wait(1.5)
    s.next_slide()
    teks_kanan = MathTex(r"\text{Perkalian Kanan: } A \otimes P_\tau \implies \text{Permutasi Kolom}", color=DARK_GRAY, font_size=32)
    teks_kanan.next_to(teorema_tex, DOWN, buff=0.8)
    mat_A2 = Matrix([
        ["1", "2", "3"],
        ["2", "3", "1"],
        ["3", "1", "2"]
    ], v_buff=0.8, h_buff=0.8).set_color(BLACK)
    mat_A2_label = MathTex("A", color=BLACK).next_to(mat_A2, DOWN, buff=0.3)
    group_A2 = VGroup(mat_A2, mat_A2_label)
    mat_P2 = Matrix([
        ["0", r"\varepsilon", r"\varepsilon"],
        [r"\varepsilon", r"\varepsilon", "0"],
        [r"\varepsilon", "0", r"\varepsilon"]
    ], v_buff=0.8, h_buff=0.8).set_color(BLACK)
    mat_P2_label = MathTex(r"P_\tau", color=BLACK).next_to(mat_P2, DOWN, buff=0.3)
    group_P2 = VGroup(mat_P2, mat_P2_label)
    mat_Res2 = Matrix([
        ["1", "3", "2"],
        ["2", "1", "3"],
        ["3", "2", "1"]
    ], v_buff=0.8, h_buff=0.8).set_color(BLACK)
    op_times2 = MathTex(r"\otimes", color=BLACK)
    op_eq2 = MathTex("=", color=BLACK)
    eq_kanan = VGroup(group_A2, op_times2, group_P2, op_eq2, mat_Res2).arrange(RIGHT, buff=0.5).next_to(teks_kanan, DOWN, buff=0.1).scale(0.7)
    op_times2.shift(UP*0.25)
    op_eq2.shift(UP*0.25)
    mat_Res2.shift(UP*0.25)

    s.play(
        Transform(teks_kiri, teks_kanan), 
        Transform(group_P, group_A2),
        Transform(op_times1, op_times2),
        Transform(group_A, group_P2),
        Transform(op_eq1, op_eq2),
        FadeOut(box_LS1), FadeOut(teks_LS1), FadeOut(mat_Res1_final),
        run_time=1
    )
    s.wait()
    s.next_slide()
    cols_A2 = mat_A2.get_columns()
    cols_Res2 = mat_Res2.get_columns()
    box_P2_c1 = SurroundingRectangle(mat_P2.get_columns()[0], color=ORANGE, buff=0.1)
    box_P2_0_1 = SurroundingRectangle(mat_P2.get_entries()[0], color=GREEN_E, buff=0.05)

    col_copy_1 = cols_A2[0].copy()
    s.play(Create(box_P2_c1), Create(box_P2_0_1),col_copy_1.animate.set_color(GREEN_E), run_time=0.8)
    
    s.play(Transform(col_copy_1, cols_Res2[0].copy().set_color(GREEN_E)), run_time=0.3)
    box_P2_c2 = SurroundingRectangle(mat_P2.get_columns()[1], color=ORANGE, buff=0.1)
    box_P2_0_2 = SurroundingRectangle(mat_P2.get_entries()[7], color=RED_E, buff=0.05)

    col_copy_3 = cols_A2[2].copy()
    s.play(
        Transform(box_P2_c1, box_P2_c2),
        Transform(box_P2_0_1, box_P2_0_2),
        col_copy_3.animate.set_color(RED_E),
        run_time=0.3
    )
    
    s.play(Transform(col_copy_3, cols_Res2[1].copy().set_color(RED_E)), run_time=0.3)
    box_P2_c3 = SurroundingRectangle(mat_P2.get_columns()[2], color=ORANGE, buff=0.1)
    box_P2_0_3 = SurroundingRectangle(mat_P2.get_entries()[5], color=BLUE_E, buff=0.05)

    col_copy_2 = cols_A2[1].copy()
    s.play(
        Transform(box_P2_c1, box_P2_c3),
        Transform(box_P2_0_1, box_P2_0_3),
        col_copy_2.animate.set_color(BLUE_E),
        run_time=0.5
    )
    
    s.play(Transform(col_copy_2, cols_Res2[2].copy().set_color(BLUE_E)), run_time=0.3)
    s.wait(1)
    s.play(
        FadeOut(box_P2_c1), FadeOut(box_P2_0_1),
        col_copy_1.animate.set_color(BLACK),
        col_copy_2.animate.set_color(BLACK),
        col_copy_3.animate.set_color(BLACK),
        run_time=0.5
    )
    mat_Res2_final = mat_Res2.copy()
    s.add(mat_Res2_final)
    s.remove(col_copy_1, col_copy_2, col_copy_3)
    box_LS2 = SurroundingRectangle(mat_Res2_final, color=PURPLE_E, buff=0.2)
    teks_LS2 = MathTex(r"\in L_S(n)", color=PURPLE_E).next_to(box_LS2, DOWN)
    s.play(Create(box_LS2), Write(teks_LS2))
    s.wait()
    s.next_slide()
    s.play(FadeOut(VGroup(teks_kiri, group_P, op_times1, group_A, op_eq1, box_LS2, teks_LS2, mat_Res2_final, judul, teorema_tex), shift=LEFT), run_time=1)

def SifatPerkalian(s):
    Mobject.set_default(color=BLACK)
    judul = Title("Perkalian Matriks Latin Square", color=BLACK, font_size=48, include_underline=True)
    judul[-1].set_color(BLACK)

    deskripsi = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Misalkan $A, B \in L_S(n)$ berturut-turut memiliki himpunan simbol""", r"""$\{a_1, a_2, \ldots, a_n\}$ dan $\{b_1, b_2, \ldots, b_n\}$ di dalam $\mathbb{R}_{\max}$""",r""". Hasil kali max-plus dari $A$ dan $B$ diberikan oleh}""", font_size=30, color=BLACK).next_to(judul, DOWN, buff=0.5)

    eq1 = VGroup(
        MathTex(r"A \otimes B =", font_size=32),
        MathTex(r"\bigoplus_{i=1}^{n} \bigoplus_{j=1}^{n}", font_size=32),
        MathTex(r"(a_i \otimes b_j)", font_size=32),
        MathTex(r"\otimes", font_size=32),
        MathTex(r"P_{\sigma_j^B \circ \sigma_i^A}", font_size=32)
    ).arrange(RIGHT, buff=0.15).next_to(deskripsi, DOWN, buff=0.5)
    s.play(Write(eq1), Write(judul), Write(deskripsi))
    s.wait(1)
    s.next_slide()

    deskripsi2 = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Misalkan $A, B \in L_S(n)$ berturut-turut memiliki himpunan simbol """, r"""$\{1, 2, \ldots, n\}$""",r""". Hasil kali max-plus dari $A$ dan $B$ diberikan oleh}""", font_size=30, color=BLACK).next_to(judul, DOWN, buff=0.5)

    eq1_new_part2 = MathTex(r"(i \otimes j)", font_size=32, color=PURE_BLUE).move_to(eq1[2])

    deskripsi2[1].set_color(PURE_BLUE)
    s.play(
        Transform(deskripsi[0], deskripsi2[0]),
        Transform(deskripsi[1], deskripsi2[1]),
        Transform(deskripsi[2], deskripsi2[2]),
        Transform(eq1[2], eq1_new_part2)
    )
    s.wait(1)
    s.next_slide()
    eq1_new_part2_plus = MathTex(r"(i + j)", font_size=32, color=PURE_BLUE).move_to(eq1[2])
    s.play(Transform(eq1[2], eq1_new_part2_plus))
    s.wait(1)
    s.next_slide()

    eq2 = VGroup(
        MathTex(r"A \otimes B =", font_size=32),
        MathTex(r"\bigoplus_{k=2}^{2n}", font_size=32),
        MathTex(r"\Bigg(", font_size=32),
        MathTex(r"\bigoplus_{\substack{i,j \in \{1,\ldots,n\} \\ i+j=k}}", font_size=32, color=PURE_BLUE),
        MathTex(r"k", font_size=32, color=PURE_BLUE),
        MathTex(r"\otimes", font_size=32),
        MathTex(r"P_{\sigma_j^B \circ \sigma_i^A}", font_size=32),
        MathTex(r"\Bigg)", font_size=32)
    ).arrange(RIGHT, buff=0.15).move_to(eq1)
    s.play(
        ReplacementTransform(eq1[0], eq2[0]),
        ReplacementTransform(eq1[1], VGroup(eq2[1], eq2[2], eq2[3])),
        ReplacementTransform(eq1[2], eq2[4]),                         
        ReplacementTransform(eq1[3], eq2[5]),                         
        ReplacementTransform(eq1[4], VGroup(eq2[6], eq2[7]))         
    )
    s.wait(1)
    s.next_slide()

    eq3 = VGroup(
        MathTex(r"A \otimes B =", font_size=32),
        MathTex(r"\bigoplus_{k=2}^{2n}", font_size=32),
        MathTex(r"k", font_size=32, color=PURE_BLUE),
        MathTex(r"\otimes", font_size=32),
        MathTex(r"\Bigg(", font_size=32),
        MathTex(r"\bigoplus_{\substack{i,j \in \{1,\ldots,n\} \\ i+j=k}}", font_size=32, color=PURE_BLUE),
        MathTex(r"P_{\sigma_j^B \circ \sigma_i^A}", font_size=32),
        MathTex(r"\Bigg)", font_size=32)
    ).arrange(RIGHT, buff=0.15).move_to(eq2)
    s.play(
        ReplacementTransform(eq2[0], eq3[0]),
        ReplacementTransform(eq2[1], eq3[1]),
        ReplacementTransform(eq2[2], eq3[4]), 
        ReplacementTransform(eq2[3], eq3[5]), 
        ReplacementTransform(eq2[4], eq3[2]), 
        ReplacementTransform(eq2[5], eq3[3]),
        ReplacementTransform(eq2[6], eq3[6]),
        ReplacementTransform(eq2[7], eq3[7])
    )
    s.wait(1)
    s.next_slide()

    catatan = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Namun setelah dianalisa lebih lanjut, hasil perkalian max-plus dari $A$ dan $B$ memiliki entri terkecil yang mungkin (minimum) sebesar $n+1$ }""", font_size=30, color=PURE_RED).next_to(eq3, DOWN, buff=0.5)

    deskripsi3 = Tex(
        r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Misalkan $A, B \in L_S(n)$ berturut-turut memiliki himpunan simbol """, 
        r"""$\{1, 2, \ldots, n\}$""",
        r""". Hasil kali max-plus dari $A$ dan $B$ """,
        r"""setelah direduksi""",
        r""" diberikan oleh}""", 
        font_size=30, color=BLACK).next_to(judul, DOWN, buff=0.5)

    deskripsi3[1].set_color(PURE_BLUE)
    deskripsi3[3].set_color(PURE_RED)

    eq_reduction = VGroup(
        MathTex(r"A \otimes B =", font_size=32),
        MathTex(r"\bigoplus_{k=n+1}^{2n}", font_size=32, color=PURE_RED),
        MathTex(r"k", font_size=32, color=PURE_BLUE),
        MathTex(r"\otimes", font_size=32),
        MathTex(r"\Bigg(", font_size=32),
        MathTex(r"\bigoplus_{\substack{i,j \in \{1,\ldots,n\} \\ i+j=k}}", font_size=32, color=PURE_BLUE),
        MathTex(r"P_{\sigma_j^B \circ \sigma_i^A}", font_size=32),
        MathTex(r"\Bigg)", font_size=32)
    ).arrange(RIGHT, buff=0.15).move_to(eq3)

    s.play(Write(catatan))
    s.play(Transform(deskripsi[0], deskripsi3[0]),
           Transform(deskripsi[1], deskripsi3[1]),
           Transform(deskripsi[2], VGroup(deskripsi3[2], deskripsi3[3], deskripsi3[4])),
           Transform(eq3[1], eq_reduction[1]))
    s.wait(1)
    s.next_slide()
    
    box = SurroundingRectangle(eq3, color=BLACK, buff=0.25)
    s.play(Create(box))
    s.wait(1)
    s.next_slide()
    s.play(FadeOut(VGroup(judul, box, catatan, deskripsi, eq3),shift=LEFT))
    
