from manim import *
from scenes.content import *
from lib.slide_tracker import *

judul = Title("Aljabar Max-Plus", color=BLACK, font_size=48, include_underline=True)
judul[-1].set_color(BLACK)

def tinjauan_pustaka(s):
#   aljabar_max_plus(s)
#   next_slide_count(s)
  matriks(s)
#   next_slide_count(s)

def matriks(s):
    my_template = TexTemplate()
    my_template.add_to_preamble(r"\usepackage{xcolor}")
    my_template.add_to_preamble(r"\usepackage{amsmath}")
    my_template.add_to_preamble(r"\usepackage{amssymb}")
    
    str_kalimat = r"""Misalkan $A = (a_{ij})$ adalah matriks berukuran $m \times n$ dan $B = (b_{ij})$ adalah matriks berukuran $n \times p$ dengan elemen-elemen dari $\mathbb{R}_{\max}$. Operasi perkalian matriks pada aljabar max-plus didefinisikan sebagai berikut:"""
    
    kalimat = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + str_kalimat + "}", color=BLACK, font_size=30, tex_template=my_template) 

    rumus_1 = MathTex(r"(A \otimes B)_{ij}", color=BLACK, font_size=30, tex_template=my_template)
    rumus_2 = MathTex(r"= \bigoplus_{k=1}^{n} (a_{ik} \otimes b_{kj})", color=BLACK, font_size=30, tex_template=my_template)
    rumus_3 = MathTex(r"= \max_{1 \leq k \leq n} (a_{ik} + b_{kj})", color=BLACK, font_size=30, tex_template=my_template).next_to(rumus_1, RIGHT, buff=0.1)
    rumus = VGroup(rumus_1, rumus_2).arrange(RIGHT, buff=0.1)
    kotak_rumus = SurroundingRectangle(Group(rumus_1, rumus_3),
                                       color=BLUE_D,
                                       fill_color=BLUE_D,
                                       fill_opacity=0.6,
                                       corner_radius=0,
                                       buff=0.2).set_z_index(-1)

    deskripsi_full = VGroup(kalimat, rumus).arrange(DOWN, buff=0.5)
    deskripsi_full.next_to(judul, DOWN, buff=0.5)

    s.play(Write(deskripsi_full), run_time=1)
    s.wait(1)
    s.next_slide()

    s.play(
        FadeOut(kalimat, shift=UP),                
        rumus.animate.next_to(judul, DOWN, buff=0.5), 
        run_time=1.5
    )
    s.wait(1)
    rumus_3.next_to(rumus_1, RIGHT, buff=0.1) 
    kotak_rumus.move_to(rumus.get_center())
    s.next_slide()
    s.play(FadeOut(rumus_2, shift=LEFT), FadeIn(rumus_3, shift=RIGHT), Write(kotak_rumus), run_time=1)

    matrix_A = [
        [2, 3],
        [4, 1]
    ]
    matrix_B = [
        [1, 5],
        [2, 3]
    ]
    

    rows_a = len(matrix_A)
    cols_a = len(matrix_A[0])
    rows_b = len(matrix_B)
    cols_b = len(matrix_B[0])

    if cols_a != rows_b:
        s.add(Text("Dimensi Error").set_color(RED))
        return

    # Hitung hasil matriks
    res_data = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            candidates = []
            for k in range(cols_a):
                val = matrix_A[i][k] + matrix_B[k][j]
                candidates.append(val)
            res_data[i][j] = max(candidates)
    
    mat_a = IntegerMatrix(matrix_A).set_color(BLACK)
    mat_b = IntegerMatrix(matrix_B).set_color(BLACK)
    mat_res = IntegerMatrix(res_data).set_color(BLACK)

    label_a = MathTex("A =", font_size=30, color=BLACK)
    label_b = MathTex("B =", font_size=30, color=BLACK)
    group_a = VGroup(label_a, mat_a.scale(0.5)).arrange(RIGHT, buff=0.2)
    group_b = VGroup(label_b, mat_b.scale(0.5)).arrange(RIGHT, buff=0.2)

    s.play(VGroup(rumus_1,rumus_3, kotak_rumus).animate.to_edge(LEFT, buff=2), run_time=1)

    group_a.next_to(rumus, RIGHT, buff=1.5)
    group_b.next_to(group_a, RIGHT, buff=0.5)
    kotak_group_a_b = SurroundingRectangle(
        Group(group_a, group_b),
        color=GREEN_D,
        fill_color=GREEN_D,
        fill_opacity=0.6,
        corner_radius=0,
        buff=0.2
    ).set_z_index(-1)

    


    s.play(Write(group_a), Write(group_b), Write(kotak_group_a_b), run_time=1)

    
    times_sym = MathTex(r"\otimes", font_size=60).set_color(BLACK)
    equals_sym = MathTex(r"=", font_size=60).set_color(BLACK)
    
    equation = VGroup(mat_a, times_sym, mat_b, equals_sym, mat_res).scale(0.8)
    equation.arrange(RIGHT, buff=0.2)
    equation.next_to(rumus_3, DOWN, buff=1)
    
    # Auto-scale agar muat di layar
    if equation.width > config.frame_width - 1:
        equation.scale_to_fit_width(config.frame_width - 1)
        
    # Sembunyikan angka hasil (opacity 0)
    for entry in mat_res.get_entries():
        entry.set_opacity(0)

    # --- 4. INTRO ANIMASI ---
    s.play(Write(mat_a), run_time=1)
    s.play(Write(times_sym), Write(mat_b), Write(equals_sym), run_time=1)
    s.play(Create(mat_res.get_brackets()), run_time=1)
    s.wait(0.5)

    # for r in range(rows_a):
    #     for c in range(cols_b):
    #         # A. Highlight Baris Matriks A & Kolom Matriks B
    #         row_obj = mat_a.get_rows()[r]
    #         col_obj = mat_b.get_columns()[c]
            
    #         rect_row = SurroundingRectangle(row_obj, color=BLUE, buff=0.1)
    #         rect_col = SurroundingRectangle(col_obj, color=GREEN, buff=0.1)
            
    #         s.play(Create(rect_row), Create(rect_col), run_time=0.5)
            
    #         # B. Buat String Rumus di Bawah
    #         parts_str = []
    #         sums_val = []
    #         for k in range(cols_a):
    #             val_a = matrix_A[r][k]
    #             val_b = matrix_B[k][c]
    #             val_sum = val_a + val_b
    #             sums_val.append(val_sum)
    #             parts_str.append(f"({val_a}+{val_b})")
            
    #         max_val = max(sums_val)
    #         inner_content = ", ".join(parts_str)
            
    #         # Rumus LaTeX: max( (a+b), (c+d) ) = hasil
    #         latex_str = f"\\max \\big( {inner_content} \\big) = {max_val}"
            
    #         step_calculation = MathTex(latex_str, font_size=34).next_to(equation, DOWN, buff=0.7)
            
    #         # Warnai angka hasil di rumus jadi kuning
    #         step_calculation[-len(str(max_val)):].set_color(YELLOW)
            
    #         s.play(Write(step_calculation), run_time=0.8)
    #         s.wait(0.5)
            
    #         # C. Pindahkan Angka dari Rumus ke Matriks Hasil
    #         entry_index = r * cols_b + c
    #         target_entry = mat_res.get_entries()[entry_index]
            
    #         # Ambil bagian angka terakhir dari rumus (source)
    #         source_part = step_calculation[-len(str(max_val)):] 
            
    #         s.play(
    #             ReplacementTransform(source_part, target_entry),
    #             target_entry.animate.set_opacity(1),
    #             run_time=0.8
    #         )
            
    #         # D. Bersihkan Highlight & Rumus untuk iterasi berikutnya
    #         s.play(
    #             FadeOut(rect_row),
    #             FadeOut(rect_col),
    #             FadeOut(step_calculation),
    #             run_time=0.4
    #         )

    # s.play(Indicate(mat_res, color=YELLOW, scale_factor=1.1), run_time=1)
    # s.wait()
    # s.next_slide()
    # s.play(FadeOut(VGroup(judul, equation)), shift=UP)
    
def derangement(s):
   pass

def aljabar_max_plus(s):
    my_template = TexTemplate()
    my_template.add_to_preamble(r"\usepackage{xcolor}")
    my_template.add_to_preamble(r"\usepackage{amsmath}")
    my_template.add_to_preamble(r"\usepackage{amssymb}")

    singkatnya = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Aljabar max-plus salah satu cabang dari aljabar tropikal 
                     yang menggunakan operasi maksimum dan penjumlahan sebagai operasi dasar.}""", color=BLACK, font_size=30, tex_template=my_template).next_to(judul, DOWN, buff=0.5)
    
    deskripsi = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""
    Aljabar max-plus salah satu cabang dari aljabar tropikal yang menggunakan operasi maksimum dan penjumlahan sebagai operasi dasar. 
    Didefinisikan himpunan $\mathbb{R}_{\max} = \mathbb{R} \cup \{-\infty\}$, $(\mathbb{R}_{\max}, \oplus, \otimes)$ disebut 
    \textit{semiring} max-plus sehingga untuk setiap $a, b \in \mathbb{R}_{\max}$ berlaku
    \begin{align*}
        a \oplus b & = \max(a, b) \\
        a \otimes b & = a + b
    \end{align*}
    Di mana elemen identitasnya adalah $\varepsilon={-\infty}$ untuk operasi $\oplus$ dan $0$ untuk operasi $\otimes$.
    }""", color=BLACK, font_size=30, tex_template=my_template).next_to(judul, DOWN, buff=0.5)

    s.play(Write(judul),Write(singkatnya))
    s.wait()
    s.next_slide()
    s.play(ReplacementTransform(singkatnya, deskripsi))
    s.wait()
    s.next_slide()
    
    axiom = Tex(
        r"\underline{Catatan}: Aksioma ", r"ring", r" meliputi", 
        color=BLACK, 
        font_size=26, 
        tex_template=my_template
    )
    axiom.move_to(deskripsi.get_bottom() + 0.5*DOWN)
    axiom.to_edge(LEFT, buff=0.5)
    
    axioms_list_1 = VGroup(
        Tex(r"$\bullet$ Tertutup terhadap $+$", color=BLACK, font_size=26, tex_template=my_template),
        Tex(r"$\bullet$ Asosiatif terhadap $+$", color=BLACK, font_size=26, tex_template=my_template),
        Tex(r"$\bullet$ Terdapat elemen identitas untuk $+$", color=BLACK, font_size=26, tex_template=my_template),
        Tex(r"$\bullet$ Terdapat elemen invers untuk $+$", color=BLACK, font_size=26, tex_template=my_template),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(axiom, DOWN, buff=0.2)
    axioms_list_1.to_edge(LEFT, buff=0.5)
    
    axioms_list_2 = VGroup(
        Tex(r"$\bullet$ Komutatif terhadap $+$", color=BLACK, font_size=26, tex_template=my_template),
        Tex(r"$\bullet$ Tertutup terhadap $\times$", color=BLACK, font_size=26, tex_template=my_template),
        Tex(r"$\bullet$ Asosiatif terhadap $\times$", color=BLACK, font_size=26, tex_template=my_template),    
        Tex(r"$\bullet$ Distributif terhadap $+$ dan $\times$", color=BLACK, font_size=26, tex_template=my_template)
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(axioms_list_1, RIGHT, buff=0.5)

    catatan = VGroup(axiom, axioms_list_1, axioms_list_2)
    catatan.to_edge(LEFT, buff=1.2)
    catatan.shift(DOWN * 0.5)
    kotak = SurroundingRectangle(
        catatan, 
        color=DARK_GRAY, 
        buff=0.3
    )
    
    s.play(Write(axiom), Write(axioms_list_1), Write(axioms_list_2), Create(kotak))
    s.wait()
    s.next_slide()

    axiom_semiring = Tex(
        r"\underline{Catatan}: Aksioma ", r"\textcolor{red}{semi}", r"ring", r" meliputi", 
        color=BLACK, 
        font_size=26, 
        tex_template=my_template
    )
    axiom_semiring.move_to(axiom.get_center())
    axiom_semiring.align_to(axiom, LEFT)

    coretan = Line(
        start=axioms_list_1[3].get_left(), 
        end=axioms_list_1[3].get_right(), 
        color=RED, 
        stroke_width=3
    )

    s.play(
        TransformMatchingTex(axiom, axiom_semiring), 
        Create(coretan),                  
        run_time=1.5
    )
    s.wait()
    s.next_slide()
    s.play(FadeOut(VGroup(
        deskripsi, axiom_semiring, axioms_list_1, axioms_list_2, kotak, coretan
    ),shift=LEFT))