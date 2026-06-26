from manim import *

from lib.slide_tracker import *


def pembahasan(s):
    # SifatPerkalian(s)
    # next_slide_count(s)
    InvariansiLatinSquare(s)
    next_slide_count(s)

def InvariansiLatinSquare(s):
    judul = Title("Invariansi Latin Square", color=BLACK, font_size=40, include_underline=True)
    judul[-1].set_color(BLACK)
    teorema_tex = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Misalkan $A\in L_S(n)$ dan misalkan $P_\sigma$, $P_\tau$ adalah matriks permutasi max-plus yang bersesuaian dengan permutasi $\sigma,\tau\in S_n$. Maka $P_\sigma\otimes A$, $A\otimes P_\tau$, dan $P_\sigma\otimes A\otimes P_\tau$ juga merupakan \textit{Latin square}.""", color=BLACK, font_size=30)
    teorema_tex.next_to(judul, DOWN, buff=0.3)
    s.play(Write(judul), Write(teorema_tex), run_time=1.5)
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

    s.play(Write(teks_kiri), Write(group_P), Write(op_times1), Write(group_A), Write(op_eq1), run_time=1.5)
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
    
