from itertools import permutations
from manim import *
from scenes.content import *
from lib.slide_tracker import *

judul_bab = Title("Aljabar Max-Plus", color=BLACK, font_size=48, include_underline=True)
judul_bab[-1].set_color(BLACK)
title_d = Title("Derangement", color=BLACK, font_size=48, include_underline=True)
title_d[-1].set_color(BLACK)

def tinjauan_pustaka(s):
    s.play(
    s.camera.frame.animate
    .move_to(ORIGIN)
    .set(width=config.frame_width)
    .set_rotation(0), 
    run_time=1.5
)
    aljabar_max_plus(s)
    next_slide_count(s)
    matriks(s)
    next_slide_count(s)
    teorema_matriks(s)
    next_slide_count(s)
    permutasi(s)
    next_slide_count(s)
    centralizer(s)
    next_slide_count(s)
    derangement(s)
    next_slide_count(s)
    S4_derangement(s)
    next_slide_count(s)
    latin_square(s)

def centralizer(s):
    judul = Title("Centralizer", color=BLACK, font_size=48, include_underline=True)
    judul[-1].set_color(BLACK)
    
    teks_atas = Tex(
    r"\parbox{"
    + str(config.frame_width)
    + r"cm}{\textbf{Definisi 3}. Centralizer dari suatu permutasi $\sigma \in S_n$ didefinisikan sebagai himpunan semua permutasi $\tau \in S_n$ yang komutatif dengan $\sigma$.}",
    color=BLACK,
    font_size=30).next_to(judul, DOWN, buff=0.5)

    definisi = MathTex(
    r"C_{S_n}(\sigma)=\{\tau\in S_n\mid\tau\sigma=\sigma\tau\}",
    color=BLACK,
    font_size=30).next_to(teks_atas, DOWN, buff=0.5)

    teks_bawah = Tex(
    r"\parbox{"
    + str(config.frame_width)
    + r"cm}{\textbf{Teorema 3}. Misalkan $\sigma\in S_n$ memiliki $a_k$ sikel berpanjang $k$ untuk setiap $k=1,2,\ldots,n$. Maka}",
    color=BLACK,
    font_size=30).next_to(definisi, DOWN, buff=0.5)

    teorema = MathTex(
        r"C_{S_n}(\sigma) \cong \prod_{k=1}^{n} \left( \mathbb{Z}_k^{a_k} \rtimes S_{a_k} \right)",
        color=BLACK, font_size=30
    ).next_to(teks_bawah, DOWN, buff=0.5)

    s.play(Write(judul), Write(teks_atas), Write(definisi),
    Write(teks_bawah), Write(teorema), run_time=1)
    s.wait(2)
    s.next_slide()
    next_slide_count(s)

    sigma_tex = MathTex(
        r"\sigma =", r"(1\;3\;4)", r"(2\;7\;8)", r"(5\;6\;9)", r"\in S_9",
        color=BLACK, font_size=42
    ).next_to(judul, DOWN, buff=0.5)

    subst_final = MathTex(
    r"C_{S_9}(\sigma)", 
    r"\cong", 
    r"\mathbb{Z}_3^3 \rtimes S_3",
    color=BLACK, font_size=42
    ).next_to(sigma_tex, DOWN, buff=0.8)
    s.play(
        ReplacementTransform(VGroup(teks_atas, definisi, teks_bawah),sigma_tex),
        ReplacementTransform(teorema, subst_final),
        run_time=1
    )
    s.wait(2)
    s.next_slide()

    grup_kiri = MathTex(r"C_{S_9}(\sigma)", color=BLUE, font_size=40).move_to(LEFT * 3.5 + UP * 0.8)
    grup_kanan = MathTex(r"\mathbb{Z}_3^3 \rtimes S_3", color=RED, font_size=40).move_to(RIGHT * 3.5 + UP * 0.8)

    s.play(
        FadeOut(subst_final[1]), 
        ReplacementTransform(subst_final[0], grup_kiri),
        ReplacementTransform(subst_final[2], grup_kanan),
        run_time=1
    )

    panah_atas = CurvedArrow(grup_kiri.get_right() + RIGHT*0.2 + UP*0.2, grup_kanan.get_left() + LEFT*0.2 + UP*0.2, angle=-TAU/12, color=GRAY)
    panah_bawah = CurvedArrow(grup_kanan.get_left() + LEFT*0.2 + DOWN*0.2, grup_kiri.get_right() + RIGHT*0.2 + DOWN*0.2, angle=-TAU/12, color=GRAY)

    label_phi = MathTex(r"\Phi", color=BLACK, font_size=32).next_to(panah_atas, UP, buff=0.1)
    label_phi_inv = MathTex(r"\Phi^{-1}", color=BLACK, font_size=32).next_to(panah_bawah, DOWN, buff=0.1)

    s.play(Create(panah_atas), Write(label_phi), Create(panah_bawah), Write(label_phi_inv))
    s.wait(1)
    s.next_slide(auto_next=True)

    kiri_group = VGroup()
    kanan_group = VGroup()

    examples = [
        (r"id", r"((0,0,0), id)"),
        (r"(1\;3\;4)", r"((1,0,0), id)"),
        (r"(2\;8\;7)", r"((0,2,0), id)"),
        (r"(1\;3\;4)(5\;6\;9)", r"((1,0,1), id)"),
        (r"(1\;2)(3\;7)(4\;8)", r"((0,0,0), (1\;2))"),
        (r"(1\;5\;3\;6\;4\;9)(2\;8\;7)", r"((1,2,0), (1\;3))"),
        (r"(1\;4\;3)(2\;9\;7\;5\;8\;6)", r"((2,2,2), (2\;3))"),
    ]

    kiri_y_start = grup_kiri.get_bottom()[1] - 0.5
    for i, (eks_kiri, eks_kanan) in enumerate(examples):
        center_kiri = MathTex(eks_kiri, color=BLUE_E, font_size=36).move_to(LEFT*2 + DOWN*1.0)
        panah_tengah = MathTex(r"\longleftrightarrow", color=BLACK, font_size=36).move_to(DOWN*1.0)
        center_kanan = MathTex(eks_kanan, color=RED_E, font_size=36).move_to(RIGHT*2 + DOWN*1.0)
        
        s.play(FadeIn(center_kiri, shift=UP), FadeIn(panah_tengah), FadeIn(center_kanan, shift=UP), run_time=0.6)
        s.wait(0.5)

        target_kiri = MathTex(eks_kiri, color=BLUE_E, font_size=28).move_to(grup_kiri.get_x() * RIGHT + (kiri_y_start - i*0.45) * UP)
        target_kanan = MathTex(eks_kanan, color=RED_E, font_size=28).move_to(grup_kanan.get_x() * RIGHT + (kiri_y_start - i*0.45) * UP)
        
        target_kiri.set_color(GRAY).set_opacity(0.3)
        target_kanan.set_color(GRAY).set_opacity(0.3)

        s.play(
            FadeOut(panah_tengah),
            Transform(center_kiri, target_kiri),
            Transform(center_kanan, target_kanan),
            run_time=0.4
        )
        kiri_group.add(center_kiri)
        kanan_group.add(center_kanan)
        s.wait(0.3)
        s.next_slide(auto_next=True)

    s.next_slide()
    vdots_kiri = MathTex(r"\vdots", color=BLUE_E, font_size=28).move_to(grup_kiri.get_x() * RIGHT + (kiri_y_start - len(examples)*0.45) * UP)
    vdots_kanan = MathTex(r"\vdots", color=RED_E, font_size=28).move_to(grup_kanan.get_x() * RIGHT + (kiri_y_start - len(examples)*0.45) * UP)
    kiri_group.add(vdots_kiri)
    kanan_group.add(vdots_kanan)
    
    kotak_kiri = SurroundingRectangle(VGroup(grup_kiri, kiri_group), color=BLUE_E, buff=0.3)
    kotak_kanan = SurroundingRectangle(VGroup(grup_kanan, kanan_group), color=RED_E, buff=0.3)

    s.play(Write(vdots_kiri), Write(vdots_kanan), Create(kotak_kiri), Create(kotak_kanan),kiri_group.animate.set_color(BLUE_E).set_opacity(1),kanan_group.animate.set_color(RED_E).set_opacity(1), run_time=1.5)
    s.wait(2)
    s.next_slide()
    s.play(FadeOut(VGroup(judul, sigma_tex, grup_kiri, grup_kanan, panah_atas, panah_bawah, label_phi, label_phi_inv, kiri_group, kanan_group, kotak_kiri, kotak_kanan), shift=LEFT))

def latin_square(s):
    judul_bab = Title("Latin Square", color=BLACK, font_size=48, include_underline=True)
    judul_bab[-1].set_color(BLACK)
    deskripsi = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Latin Square adalah susunan $n \times n$ yang diisi dengan $n$ simbol berbeda,
                sehingga setiap simbol muncul tepat satu kali di setiap baris dan tepat satu kali di setiap kolom.}""", color=BLACK, font_size=30).next_to(judul_bab, DOWN, buff=0.5)
    s.play(Write(judul_bab), Write(deskripsi), run_time=1)

    n = 4
    square_size = 1.0
    
    grid_data = [
        [1, 2, 3, 4], 
        [2, 1, 4, 3], 
        [3, 4, 1, 2], 
        [4, 3, 2, 1]  
    ]
    
    color_map = {
        1: TEAL_C,
        2: RED_C,
        3: GREEN_C,
        4: ORANGE
    }
    grid_group = VGroup()
    cells = {} 
    number_mobjects = {} 
    
    for r in range(n):
        for c in range(n):
            sq = Square(side_length=square_size, color=DARK_GRAY, stroke_width=2)
            pos = np.array([c * square_size - (n/2 * square_size) + square_size/2, 
                            -r * square_size + (n/2 * square_size) - square_size/2, 
                            0])
            sq.move_to(pos)
            grid_group.add(sq)
            cells[(r, c)] = sq
    grid_group.next_to(deskripsi, DOWN, buff=0.5)
    s.play(Create(grid_group), run_time=1)
    
    row1_anims = []
    for c in range(n):
        val = grid_data[0][c]
        num_obj = MathTex(str(val), color=BLACK, font_size=42)
        num_obj.move_to(cells[(0, c)])
        num_obj.set_z_index(1) 
        number_mobjects[(0, c)] = num_obj
        row1_anims.append(Write(num_obj))
        
    s.play(AnimationGroup(*row1_anims, lag_ratio=0.1), run_time=1)
    s.wait(0.3)
    for r in range(1, n):
        anims = []
        for c in range(n):
            target_val = grid_data[r][c]
            target_cell = cells[(r, c)]
            
            source_obj = None
            for prev_c in range(n):
                if grid_data[r-1][prev_c] == target_val:
                    source_obj = number_mobjects[(r-1, prev_c)]
                    break
            
            final_num = MathTex(str(target_val), color=BLACK, font_size=42)
            final_num.move_to(target_cell)
            final_num.set_z_index(1)
            number_mobjects[(r, c)] = final_num
            
            anims.append(
                TransformFromCopy(
                    source_obj, 
                    final_num, 
                    path_arc=-PI/2
                )
            )
        s.play(AnimationGroup(*anims), run_time=1.2)
        s.wait(0.2)
    s.wait(0.5)
    coloring_anims = []
    for r in range(n):
        for c in range(n):
            val = grid_data[r][c]
            color = color_map[val]
            cell = cells[(r, c)]
            
            coloring_anims.append(
                cell.animate.set_fill(color, opacity=0.5).set_stroke(opacity=1)
            )
    s.play(LaggedStart(*coloring_anims, lag_ratio=0.05), run_time=2)
    s.wait(2)
    s.next_slide()
    s.play(FadeOut(VGroup(deskripsi, grid_group, *number_mobjects.values()), shift=LEFT), run_time=1)

    banyak_LS = Tex(r"Jumlah Latin squares berordo $n$ \textbf{(OEIS A002860)}", color=BLACK, font_size=30)
    banyak_LS.next_to(judul_bab, DOWN, buff=0.3)
    
    table_data_left = [
        ["1", "1"],
        ["2", "2"],
        ["3", "12"],
        ["4", "576"],
        ["5", r"161\,280"]
    ]
    
    table_data_right = [
        ["6", r"812\,851\,200"],
        ["7", r"61\,479\,419\,904\,000"],
        ["8", r"108\,776\,032\,459\,082\,956\,800"],
        ["9", r"5\,524\,751\,496\,156\,892\,842\,531\,225\,600"],
        ["10", r"9\,982\,437\,658\,213\,039\,877\,725\,064\,756\,920\,320\,000"]
    ]
    
    table_left = Table(
        table_data_left,
        col_labels=[MathTex("n"), Tex("Jumlah Latin square")],
        include_outer_lines=True,
        line_config={"color": BLACK},
        element_to_mobject=Tex
    )
    table_left.get_entries().set_color(BLACK)
    table_left.get_col_labels().set_color(BLACK)
    
    table_right = Table(
        table_data_right,
        col_labels=[MathTex("n"), Tex("Jumlah Latin square")],
        include_outer_lines=True,
        line_config={"color": BLACK},
        element_to_mobject=Tex
    )
    table_right.get_entries().set_color(BLACK)
    table_right.get_col_labels().set_color(BLACK)
    
    table_group = VGroup(table_left, table_right).arrange(RIGHT, buff=0.8)
    
    # Highlight the header row
    for t in [table_left, table_right]:
        t.add_highlighted_cell((1, 1), color=GRAY, fill_opacity=0.4)
        t.add_highlighted_cell((1, 2), color=GRAY, fill_opacity=0.4)
    
    # Scale table group to fit nicely on screen
    table_group.scale(0.55).next_to(banyak_LS, DOWN, buff=0.2)
    
    if table_group.height > config.frame_height - 1.5:
        table_group.height = config.frame_height - 1.5
    if table_group.width > config.frame_width - 1:
        table_group.width = config.frame_width - 1
        
    s.play(Write(banyak_LS), Create(table_group))
    s.wait(1)
    s.next_slide()
    s.play(FadeOut(VGroup(banyak_LS, table_group), shift=LEFT), run_time=1)
    next_slide_count(s)

    deskripsi_baru = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Setiap Latin Square dapat didekomposisi menjadi penjumlahan matriks permutasi max--plus.
                         Matriks permutasi bersesuaian dengan permutasi yang merepresentasikan posisi simbol pada setiap baris.
                         }""", color=BLACK, font_size=30).next_to(judul_bab, DOWN, buff=0.5)
    s.play(Write(deskripsi_baru), run_time=1)
    s.wait(1)
    s.next_slide(auto_next=True)
    scale_fac = 0.8
    matrix_vals = [
        [2, 3, 1],
        [1, 2, 3],
        [3, 1, 2]
    ]
    n = 3
    
    val_colors = {
        1: BLUE,
        2: RED,
        3: GREEN_E
    }
    label_A = MathTex("A =", color=BLACK, font_size=40)
    
    m_A = Matrix(matrix_vals, v_buff=0.5, h_buff=0.6, left_bracket="(", right_bracket=")")
    m_A.set_color(BLACK)
    m_A.scale(scale_fac)
    
    eq_sign = MathTex("=", color=BLACK, font_size=40)
    terms = []
    operators = []
    p_matrices = [] 
    for k in range(1, 4):
        scalar_tex = MathTex(str(k), color=val_colors[k], font_size=40)
        otimes = MathTex(r"\otimes", color=BLACK, font_size=50)
        
        p_vals = [[r"\varepsilon" for _ in range(n)] for _ in range(n)]
        
        target_indices = []
        for r in range(n):
            for c in range(n):
                if matrix_vals[r][c] == k:
                    p_vals[r][c] = "0"
                    target_indices.append((r, c))
        m_P = Matrix(p_vals, v_buff=0.5, h_buff=0.5, left_bracket="(", right_bracket=")")
        m_P.set_color(BLACK)
        m_P.scale(scale_fac)
        for r in range(n):
            for c in range(n):
                idx = r * n + c
                ent = m_P.get_entries()[idx]
                if (r, c) in target_indices:
                    ent.set_color(val_colors[k])
                else:
                    ent.set_color(GRAY_C)
        
        p_matrices.append((m_P, target_indices))
        term_group = VGroup(scalar_tex, otimes, m_P).arrange(RIGHT, buff=0.15)
        terms.append(term_group)
        if k < 3:
            oplus = MathTex(r"\oplus", color=BLACK, font_size=50)
            operators.append(oplus)
    full_equation = VGroup(label_A, m_A, eq_sign)
    for i in range(3):
        full_equation.add(terms[i])
        if i < 2:
            full_equation.add(operators[i])
    full_equation.arrange(RIGHT, buff=0.2)
    
    target_width = config.frame_width - 1
    if full_equation.width > target_width:
        full_equation.scale_to_fit_width(target_width)
    
    full_equation.next_to(deskripsi_baru, DOWN, buff=1.0)
    s.play(Write(label_A), Create(m_A))
    s.play(Write(eq_sign))
    s.next_slide(loop=True)
    for k in range(1, 4):
        m_P, target_indices = p_matrices[k-1]
        term_group = terms[k-1]
        scalar = term_group[0]
        otimes = term_group[1]
        
        highlights = []
        entries_A = m_A.get_entries()
        
        for r, c in target_indices:
            idx = r * n + c
            entry = entries_A[idx]
            rect = SurroundingRectangle(entry, color=val_colors[k], buff=0.08, stroke_width=2)
            highlights.append(rect)
        s.play(
            LaggedStart(*[Create(h) for h in highlights], lag_ratio=0.1),
            run_time=0.5
        )
        s.play(
            TransformFromCopy(VGroup(*highlights), m_P),
            Write(scalar),
            Write(otimes),
            run_time=1
        )
        
        s.play(FadeOut(VGroup(*highlights)), run_time=0.3)
        if k < 3:
            s.play(Write(operators[k-1]), run_time=0.5)

    s.wait(5)
    cycle_notations = [
        r"(1 \ 3 \ 2)", 
        r"(1)", 
        r"(1 \ 2 \ 3)"
        ]

    cycle_group = VGroup()

    for i in range(3):
        matrix_obj = terms[i][2] 
        brace = Brace(matrix_obj, direction=DOWN, color=BLACK)
        perm_label = MathTex(cycle_notations[i], color=val_colors[i+1], font_size=36)
        perm_label.next_to(brace, DOWN, buff=0.1)
        cycle_group.add(brace, perm_label)

    s.next_slide()

    s.play(Write(cycle_group), run_time=1.5)
    s.wait()
    
    s.next_slide()
    s.play(FadeOut(VGroup(full_equation, deskripsi_baru, cycle_group, judul_bab), scale=0.5), run_time=1)

def permutasi(s):
    judul_bab = Title("Permutasi", color=BLACK, font_size=48, include_underline=True)
    judul_bab[-1].set_color(BLACK)
    deskripsi = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Suatu permutasi pada himpunan hingga $X$ adalah fungsi bijektif
                $\sigma : X \to X$.
                Jika $X = \{1,2,\ldots,n\}$, maka himpunan semua permutasi pada $X$
                membentuk grup simetri $S_n$ terhadap operasi komposisi.}""", color=BLACK, font_size=30).next_to(judul_bab, DOWN, buff=0.5)

    s.play(Write(judul_bab), Write(deskripsi), run_time=1)

    inputs = [1, 2, 3, 4, 5, 6]
    outputs = [3, 5, 1, 2, 6, 4] 
    n = len(inputs)
    matrix_content = VGroup().move_to(ORIGIN)
    top_row_refs = [] 
    bot_row_refs = []
    for i in range(n):
        t_tex = MathTex(str(inputs[i]), color=BLUE, font_size=36)
        b_tex = MathTex(str(outputs[i]), color=RED, font_size=36)
        
        col = VGroup(t_tex, b_tex).arrange(DOWN, buff=0.35)
        
        matrix_content.add(col)
        top_row_refs.append(t_tex)
        bot_row_refs.append(b_tex)
    matrix_content.arrange(RIGHT, buff=0.5)
    bracket_height = matrix_content.height + 0.2
    
    left_bracket = MathTex("(", color=BLACK).stretch_to_fit_height(bracket_height)
    right_bracket = MathTex(")", color=BLACK).stretch_to_fit_height(bracket_height)
    
    left_bracket.next_to(matrix_content, LEFT, buff=0.15)
    right_bracket.next_to(matrix_content, RIGHT, buff=0.15)
    sigma_label = MathTex(r"\sigma =", color=BLACK, font_size=40).next_to(left_bracket, LEFT, buff=0.2)
    full_matrix_group = VGroup(sigma_label, left_bracket, matrix_content, right_bracket)
    
    full_matrix_group.to_edge(LEFT, buff=1.0)
    s.next_slide(auto_next=True)
    s.play(
        Write(sigma_label),
        Write(left_bracket),
        Write(right_bracket),
        LaggedStart(*[Write(col) for col in matrix_content], lag_ratio=0.1)
    )
    s.wait(0.5)
    equals_sign = MathTex("=", color=BLACK, font_size=40)
    equals_sign.next_to(full_matrix_group, RIGHT, buff=0.3)
    
    s.play(Write(equals_sign))
    s.next_slide(loop=True)
    
    visited = [False] * n
    cursor_box = SurroundingRectangle(top_row_refs[0], color=ORANGE, buff=0.08, stroke_width=2)
    
    last_mobject = equals_sign
    cycle_group = VGroup()
    
    for i in range(n):
        if visited[i]:
            continue
        cycle_start_val = inputs[i]
        current_val = cycle_start_val
        curr_idx = i
        open_paren = MathTex("(", color=BLACK, font_size=36)
        open_paren.next_to(last_mobject, RIGHT, buff=0.15)
        s.play(Write(open_paren), run_time=0.4)
        last_mobject = open_paren
        cycle_group.add(open_paren)
        first_in_cycle = True
        while True:
            visited[curr_idx] = True
            
            target_top = top_row_refs[curr_idx]
            target_bot = bot_row_refs[curr_idx]
            s.play(
                cursor_box.animate.move_to(target_top),
                target_top.animate.set_color(ORANGE),
                run_time=0.4
            )
            arrow_down = Arrow(target_top.get_bottom(), target_bot.get_top(), color=ORANGE, buff=0.05, max_tip_length_to_length_ratio=0.4)
            s.play(GrowArrow(arrow_down), run_time=0.2)
            s.play(target_bot.animate.set_color(ORANGE), run_time=0.2)
            if first_in_cycle:
                cycle_num = MathTex(str(current_val), color=BLACK, font_size=36)
                cycle_num.next_to(last_mobject, RIGHT, buff=0.1)
                s.play(TransformFromCopy(target_top, cycle_num), run_time=0.5)
                last_mobject = cycle_num
                cycle_group.add(cycle_num)
                first_in_cycle = False
            
            next_val = outputs[curr_idx]
            if next_val == cycle_start_val:
                close_paren = MathTex(")", color=BLACK, font_size=36)
                close_paren.next_to(last_mobject, RIGHT, buff=0.1)
                s.play(Write(close_paren), FadeOut(arrow_down), run_time=0.4)
                last_mobject = close_paren
                cycle_group.add(close_paren)
                
                s.play(cursor_box.animate.set_opacity(0), run_time=0.2)
                break
            else:
                cycle_num = MathTex(str(next_val), color=BLACK, font_size=36)
                cycle_num.next_to(last_mobject, RIGHT, buff=0.25)
                
                s.play(TransformFromCopy(target_bot, cycle_num), FadeOut(arrow_down), run_time=0.5)
                last_mobject = cycle_num
                cycle_group.add(cycle_num)
                
                next_idx = inputs.index(next_val)
                next_top_target = top_row_refs[next_idx]
                
                path_arc = CurvedArrow(target_bot.get_bottom(), next_top_target.get_bottom(), angle=-TAU/3, color=GRAY_C, stroke_width=2)
                
                s.play(Create(path_arc), run_time=0.5)
                s.play(FadeOut(path_arc), run_time=0.2)
                
                current_val = next_val
                curr_idx = next_idx
        for r in range(len(top_row_refs)):
             if visited[r]:
                 top_row_refs[r].set_color(BLUE_E).set_opacity(0.3)
                 bot_row_refs[r].set_color(RED_E).set_opacity(0.3)
    
    total_group = VGroup(full_matrix_group, equals_sign, cycle_group)
    s.play(
        AnimationGroup(
             *[t.animate.set_opacity(1).set_color(BLACK) for t in top_row_refs],
             *[b.animate.set_opacity(1).set_color(BLACK) for b in bot_row_refs],
             lag_ratio=0.05
         ), run_time=0.5
    )
    s.play(total_group.animate.move_to(ORIGIN),run_time=0.5)
    s.play(Circumscribe(cycle_group), run_time=0.5, color=DARK_BROWN)
    s.wait()
    s.next_slide()
    next_slide_count(s)
    judul_bab_baru = Text("Matriks Permutasi", color=BLACK, font_size=38).move_to(judul_bab[0])
    s.play(FadeOut(VGroup(full_matrix_group, equals_sign, cycle_group, deskripsi), shift=LEFT), 
           Transform(judul_bab[0], judul_bab_baru),run_time=1)
    deskripsi_baru = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Misalkan $\sigma \in S_n$ suatu permutasi.
                        Matriks $P_\sigma = (p_{ij}) \in \mathbb{R}_{\max}^{\,n \times n}$
                        disebut \emph{matriks permutasi max--plus} yang bersesuaian dengan $\sigma$
                        jika
                        \[
                        p_{ij} =
                        \begin{cases}
                        0, & \text{jika } j = \sigma(i),\\
                        -\infty, & \text{jika } j \neq \sigma(i).
                        \end{cases}
                        \]""", color=BLACK, font_size=30).next_to(judul_bab[0], DOWN, buff=0.5)
    s.play(Write(deskripsi_baru), run_time=1)
    s.wait(1)
    s.next_slide(auto_next=True)

    n = 6
    matrix_data = [[r"\varepsilon" for _ in range(n)] for _ in range(n)]
    
    matrix_mobj = Matrix(
        matrix_data, 
        v_buff=0.6, 
        h_buff=0.8, 
        element_alignment_corner=ORIGIN,
        left_bracket="[", 
        right_bracket="]"
    )
    matrix_mobj.set_color(BLACK) 
    
    for entry in matrix_mobj.get_entries():
        entry.set_color(GRAY_C)
    matrix_mobj.scale(0.6)
    matrix_mobj.next_to(deskripsi_baru, DOWN, buff=1)
    matrix_mobj.shift(RIGHT * 3)
    row_labels = VGroup()
    col_labels = VGroup()
    for i in range(n):
        row_ref = matrix_mobj.get_rows()[i]
        lbl_r = MathTex(str(i+1), color=BLUE_E, font_size=20)
        lbl_r.next_to(row_ref, RIGHT, buff=0.4)
        row_labels.add(lbl_r)
        col_ref = matrix_mobj.get_columns()[i]
        lbl_c = MathTex(str(i+1), color=RED_E, font_size=20)
        lbl_c.next_to(col_ref, DOWN, buff=0.3)
        col_labels.add(lbl_c)
    p_sigma_label = MathTex(r"P_{\sigma} =", color=BLACK, font_size=40).next_to(matrix_mobj, LEFT, buff=0.5)
    
    sigma_label = MathTex(r"\sigma =", color=BLACK, font_size=40)
    
    cycle_tex_strings = [
        "(", "1", "3", ")", 
        "(", "2", "5", "6", "4", ")"
    ]
    
    cycle_group = VGroup()
    for ss in cycle_tex_strings:
        cycle_group.add(MathTex(ss, color=BLACK, font_size=40))
    
    cycle_group.arrange(RIGHT, buff=0.2)
    
    sigma_full = VGroup(sigma_label, cycle_group).arrange(RIGHT, buff=0.2)
    sigma_full.next_to(p_sigma_label, LEFT, buff=1.0)
    s.play(
        Write(p_sigma_label),
        Create(matrix_mobj),
        Write(row_labels),
        Write(col_labels),
        Write(sigma_full))
    s.wait(1)
    s.next_slide(loop=True)
    mappings = [
        (1, 3, cycle_group[1], cycle_group[2]), 
        (3, 1, cycle_group[2], cycle_group[1]), 
        (2, 5, cycle_group[5], cycle_group[6]), 
        (5, 6, cycle_group[6], cycle_group[7]), 
        (6, 4, cycle_group[7], cycle_group[8]), 
        (4, 2, cycle_group[8], cycle_group[5]), 
    ]
    entries = matrix_mobj.get_entries()
    for inp, out, mob_in, mob_out in mappings:
        idx = (inp - 1) * n + (out - 1) 
        target_entry = entries[idx]

        s.play(
            mob_in.animate.set_color(BLUE).scale(1.2), 
            mob_out.animate.set_color(RED).scale(1.2),  
            row_labels[inp-1].animate.set_color(BLUE).set_weight(BOLD).scale(1.2),
            col_labels[out-1].animate.set_color(RED).set_weight(BOLD).scale(1.2),
            run_time=0.4
        )
        
        indicator = SurroundingRectangle(target_entry, color=ORANGE, buff=0.15)
        s.play(Create(indicator), run_time=0.2)
        
        new_val = MathTex("0", color=BLACK, font_size=32).move_to(target_entry)
        
        s.play(
            Transform(target_entry, new_val),
            run_time=0.4
        )
        
        s.play(
            mob_in.animate.set_color(BLACK).scale(1/1.2),
            mob_out.animate.set_color(BLACK).scale(1/1.2),
            row_labels[inp-1].animate.set_color(BLUE).scale(1/1.2), 
            col_labels[out-1].animate.set_color(RED).scale(1/1.2),
            FadeOut(indicator),
            run_time=0.3
        )
    s.play(
        FadeOut(row_labels),
        FadeOut(col_labels),
        run_time=1
    )
    s.play(
        matrix_mobj.get_entries().animate.set_color(BLACK),
        run_time=1
    )
    final_box = SurroundingRectangle(VGroup(p_sigma_label, matrix_mobj), color=GREEN, buff=0.2)
    s.play(Create(final_box))
    s.wait(2)
    s.next_slide()
    s.play(FadeOut(VGroup(p_sigma_label, matrix_mobj, sigma_full, final_box, deskripsi_baru), shift=LEFT), run_time=1)

    next_slide_count(s)

    teks_awal = Tex(r"\parbox{" + str(config.frame_width-1) + r"cm}{Misalkan $\mathcal{P}_n$ adalah himpunan seluruh matriks permutasi max-plus berukuran $n \times n$. Untuk setiap permutasi $\alpha, \beta \in S_n$, berlaku sifat perkalian:}", color=BLACK, font_size=32).next_to(judul_bab, DOWN, buff=0.4)
    
    rumus_awal = MathTex(
        r"P_\alpha", r"\otimes", r"P_\beta", r"=", r"P_{\beta \circ \alpha}",
        color=BLACK, font_size=40
    ).next_to(teks_awal, DOWN, buff=0.4)
    s.play(Write(teks_awal))
    s.play(Write(rumus_awal))
    s.wait(1)
    s.next_slide()
    e = r"\varepsilon"
    A_entries = [[e]*4 for _ in range(4)]
    A_entries[0][3] = "0"; A_entries[1][2] = "0"; A_entries[2][0] = "0"; A_entries[3][1] = "0"
    mat_A = Matrix(A_entries, element_to_mobject_config={"color": BLACK}).scale(0.6)
    mat_A.get_brackets().set_color(BLACK)
    B_entries = [[e]*4 for _ in range(4)]
    B_entries[0][1] = "0"; B_entries[1][0] = "0"; B_entries[2][3] = "0"; B_entries[3][2] = "0"
    mat_B = Matrix(B_entries, element_to_mobject_config={"color": BLACK}).scale(0.6)
    mat_B.get_brackets().set_color(BLACK)
    C_entries = [[e]*4 for _ in range(4)]
    C_entries[0][2] = "0"; C_entries[1][3] = "0"; C_entries[2][1] = "0"; C_entries[3][0] = "0"
    mat_C = Matrix(C_entries, element_to_mobject_config={"color": BLACK}).scale(0.6)
    mat_C.get_brackets().set_color(BLACK)

    lbl_A = MathTex(r"P_\alpha", color=BLACK, font_size=36)
    lbl_B = MathTex(r"P_\beta", color=BLACK, font_size=36)
    lbl_C = MathTex(r"P_{\beta \circ \alpha}", color=BLACK, font_size=36)
    otimes_target = MathTex(r"\otimes", color=BLACK, font_size=40)
    eq_target = MathTex(r"=", color=BLACK, font_size=40)

    group_matrices = VGroup(mat_A, otimes_target, mat_B, eq_target, mat_C).arrange(RIGHT, buff=0.2).next_to(judul_bab, DOWN, buff=1.0)
    
    lbl_A.next_to(mat_A, UP, buff=0.2)
    lbl_B.next_to(mat_B, UP, buff=0.2)
    lbl_C.next_to(mat_C, UP, buff=0.2)

    s.play(
        ReplacementTransform(teks_awal, VGroup(mat_A, mat_B, mat_C)),
        ReplacementTransform(rumus_awal[0], lbl_A),
        ReplacementTransform(rumus_awal[1], otimes_target),
        ReplacementTransform(rumus_awal[2], lbl_B),
        ReplacementTransform(rumus_awal[3], eq_target),
        ReplacementTransform(rumus_awal[4], lbl_C),
        run_time=1
    )
    s.wait(1)
    s.next_slide(auto_next=True)

    mappings = [
        (1, 4, 3), 
        (2, 3, 4), 
        (3, 1, 2), 
        (4, 2, 1)  
    ]

    i_val, k_val, j_val = mappings[0]
    i_idx, k_idx, j_idx = i_val - 1, k_val - 1, j_val - 1

    eq_1 = MathTex(
        r"[P_\alpha]_{", str(i_val), r",", str(k_val), r"} = 0 \iff \alpha(", str(i_val), r") = ", str(k_val), 
        color=BLACK, font_size=32
    )
    eq_1[1].set_color(RED_E); eq_1[3].set_color(BLUE_E); eq_1[5].set_color(RED_E); eq_1[7].set_color(BLUE_E)
    eq_2 = MathTex(
        r"[P_\beta]_{", str(k_val), r",", str(j_val), r"} = 0 \iff \beta(", str(k_val), r") = ", str(j_val), 
        color=BLACK, font_size=32
    )
    eq_2[1].set_color(BLUE_E); eq_2[3].set_color(GREEN_E); eq_2[5].set_color(BLUE_E); eq_2[7].set_color(GREEN_E)
    group_eq = VGroup(eq_1, eq_2).arrange(RIGHT, buff=1.0).next_to(group_matrices, DOWN, buff=1.0)
    
    eq_3 = MathTex(
        r"(\beta \circ \alpha)(", str(i_val), r") = \beta(\alpha(", str(i_val), r")) = \beta(", str(k_val), r") = ", str(j_val), 
        color=BLACK, font_size=32
    )
    eq_3[1].set_color(RED_E); eq_3[3].set_color(RED_E); eq_3[5].set_color(BLUE_E); eq_3[7].set_color(GREEN_E)
    eq_4 = MathTex(
        r"\Longrightarrow [P_{\beta \circ \alpha}]_{", str(i_val), r",", str(j_val), r"} = 0", 
        color=BLACK, font_size=32
    )
    eq_4[1].set_color(RED_E); eq_4[3].set_color(GREEN_E)
    
    group_eq2 = VGroup(eq_3, eq_4).arrange(RIGHT, buff=0.2).next_to(group_eq, DOWN, buff=0.4)
    
    box_row_A = SurroundingRectangle(mat_A.get_rows()[i_idx], color=RED_E, buff=0.1)
    box_col_B = SurroundingRectangle(mat_B.get_columns()[j_idx], color=GREEN_E, buff=0.1)
    
    label_i = MathTex(f"i={i_val}", color=RED_E, font_size=20).next_to(mat_A, LEFT, buff=0.15).match_y(mat_A.get_rows()[i_idx])
    label_k1 = MathTex(f"k={k_val}", color=BLUE_E, font_size=20).next_to(mat_A, DOWN, buff=0.15).match_x(mat_A.get_columns()[k_idx])
    
    label_k2 = MathTex(f"k={k_val}", color=BLUE_E, font_size=20).next_to(mat_B, LEFT, buff=0.1).match_y(mat_B.get_rows()[k_idx])
    label_j = MathTex(f"j={j_val}", color=GREEN_E, font_size=20).next_to(mat_B, DOWN, buff=0.15).match_x(mat_B.get_columns()[j_idx])
    elem_A = mat_A.get_entries()[i_idx * 4 + k_idx]
    elem_B = mat_B.get_entries()[k_idx * 4 + j_idx]
    elem_C = mat_C.get_entries()[i_idx * 4 + j_idx]
    
    box_row_C = SurroundingRectangle(mat_C.get_rows()[i_idx], color=RED_E, buff=0.1)
    box_col_C = SurroundingRectangle(mat_C.get_columns()[j_idx], color=GREEN_E, buff=0.1)
    label_i_C = MathTex(f"i={i_val} ", color=RED_E, font_size=20).next_to(mat_C, RIGHT, buff=0.15).match_y(mat_C.get_rows()[i_idx])
    label_j_C = MathTex(f"j={j_val}", color=GREEN_E, font_size=20).next_to(mat_C, DOWN, buff=0.15).match_x(mat_C.get_columns()[j_idx])

    rt = 0.6
    s.play(Write(label_i), Create(box_row_A),Write(label_k1),elem_A.animate.set_color(BLUE_E), TransformFromCopy(elem_A, eq_1), run_time=rt)
    s.play(Write(label_j), Create(box_col_B), Write(label_k2), elem_B.animate.set_color(BLUE_E), TransformFromCopy(elem_B, eq_2), run_time=rt)
    s.play(Write(group_eq2), run_time=rt)
    s.play(Write(label_i_C), Write(label_j_C), Create(box_row_C), Create(box_col_C),elem_C.animate.set_color(BLUE_D), run_time=rt)
    s.play(Indicate(eq_4, color=BLUE_D), run_time=rt)
    s.wait(1)

    prev_label_i, prev_box_row_A, prev_label_k1, prev_eq_1 = label_i, box_row_A, label_k1, eq_1
    prev_label_k2, prev_box_col_B, prev_label_j, prev_eq_2 = label_k2, box_col_B, label_j, eq_2
    prev_eq_3, prev_eq_4 = eq_3, eq_4
    prev_label_i_C, prev_label_j_C, prev_box_row_C, prev_box_col_C = label_i_C, label_j_C, box_row_C, box_col_C
    prev_elem_A, prev_elem_B, prev_elem_C = elem_A, elem_B, elem_C

    s.next_slide(loop=True)

    ping_pong_sequence = [1, 2, 3, 2, 1, 0]
    rt_shift = 0.6

    for p_idx in ping_pong_sequence:
        i_val, k_val, j_val = mappings[p_idx]
        i_idx, k_idx, j_idx = i_val - 1, k_val - 1, j_val - 1

        # Target Objects
        t_eq_1 = MathTex(r"[P_\alpha]_{", str(i_val), r",", str(k_val), r"} = 0 \iff \alpha(", str(i_val), r") = ", str(k_val), color=BLACK, font_size=32)
        t_eq_1[1].set_color(RED_E); t_eq_1[3].set_color(BLUE_E); t_eq_1[5].set_color(RED_E); t_eq_1[7].set_color(BLUE_E)
        t_eq_2 = MathTex(r"[P_\beta]_{", str(k_val), r",", str(j_val), r"} = 0 \iff \beta(", str(k_val), r") = ", str(j_val), color=BLACK, font_size=32)
        t_eq_2[1].set_color(BLUE_E); t_eq_2[3].set_color(GREEN_E); t_eq_2[5].set_color(BLUE_E); t_eq_2[7].set_color(GREEN_E)
        t_group_eq = VGroup(t_eq_1, t_eq_2).arrange(RIGHT, buff=1.0).next_to(group_matrices, DOWN, buff=1.0)
        
        t_eq_3 = MathTex(r"(\beta \circ \alpha)(", str(i_val), r") = \beta(\alpha(", str(i_val), r")) = \beta(", str(k_val), r") = ", str(j_val), color=BLACK, font_size=32)
        t_eq_3[1].set_color(RED_E); t_eq_3[3].set_color(RED_E); t_eq_3[5].set_color(BLUE_E); t_eq_3[7].set_color(GREEN_E)
        t_eq_4 = MathTex(r"\Longrightarrow [P_{\beta \circ \alpha}]_{", str(i_val), r",", str(j_val), r"} = 0", color=BLACK, font_size=32)
        t_eq_4[1].set_color(RED_E); t_eq_4[3].set_color(GREEN_E)
        t_group_eq2 = VGroup(t_eq_3, t_eq_4).arrange(RIGHT, buff=0.2).next_to(t_group_eq, DOWN, buff=0.4)
        
        t_box_row_A = SurroundingRectangle(mat_A.get_rows()[i_idx], color=RED_E, buff=0.1)
        t_box_col_B = SurroundingRectangle(mat_B.get_columns()[j_idx], color=GREEN_E, buff=0.1)
        
        t_label_i = MathTex(f"i={i_val}", color=RED_E, font_size=20).next_to(mat_A, LEFT, buff=0.15).match_y(mat_A.get_rows()[i_idx])
        t_label_k1 = MathTex(f"k={k_val}", color=BLUE_E, font_size=20).next_to(mat_A, DOWN, buff=0.15).match_x(mat_A.get_columns()[k_idx])
        
        t_label_k2 = MathTex(f"k={k_val}", color=BLUE_E, font_size=20).next_to(mat_B, LEFT, buff=0.1).match_y(mat_B.get_rows()[k_idx])
        t_label_j = MathTex(f"j={j_val}", color=GREEN_E, font_size=20).next_to(mat_B, DOWN, buff=0.15).match_x(mat_B.get_columns()[j_idx])
        
        elem_A = mat_A.get_entries()[i_idx * 4 + k_idx]
        elem_B = mat_B.get_entries()[k_idx * 4 + j_idx]
        elem_C = mat_C.get_entries()[i_idx * 4 + j_idx]
        
        t_box_row_C = SurroundingRectangle(mat_C.get_rows()[i_idx], color=RED_E, buff=0.1)
        t_box_col_C = SurroundingRectangle(mat_C.get_columns()[j_idx], color=GREEN_E, buff=0.1)
        t_label_i_C = MathTex(f"i={i_val} ", color=RED_E, font_size=20).next_to(mat_C, RIGHT, buff=0.15).match_y(mat_C.get_rows()[i_idx])
        t_label_j_C = MathTex(f"j={j_val}", color=GREEN_E, font_size=20).next_to(mat_C, DOWN, buff=0.15).match_x(mat_C.get_columns()[j_idx])

        # Matikan highlight warna sebelumnya
        s.play(
            prev_elem_A.animate.set_color(BLACK),
            prev_elem_B.animate.set_color(BLACK),
            prev_elem_C.animate.set_color(BLACK), # Reset C juga agar loop bisa mulus ke posisi awal
            run_time=0.2
        )
        
        s.play(
            Transform(prev_label_i, t_label_i),
            Transform(prev_box_row_A, t_box_row_A),
            Transform(prev_label_k1, t_label_k1),
            Transform(prev_eq_1, t_eq_1),
            
            Transform(prev_label_k2, t_label_k2),
            Transform(prev_box_col_B, t_box_col_B),
            Transform(prev_label_j, t_label_j),
            Transform(prev_eq_2, t_eq_2),
            
            Transform(prev_eq_3, t_eq_3),
            Transform(prev_eq_4, t_eq_4),
            
            Transform(prev_label_i_C, t_label_i_C),
            Transform(prev_box_row_C, t_box_row_C),
            Transform(prev_label_j_C, t_label_j_C),
            Transform(prev_box_col_C, t_box_col_C),
            
            run_time=rt_shift
        )
        
        s.play(
            elem_A.animate.set_color(BLUE_E),
            elem_B.animate.set_color(BLUE_E),
            elem_C.animate.set_color(BLUE_D),
            Indicate(prev_eq_4, color=BLUE_D), 
            run_time=0.4
        )
        s.wait(0.5)

        prev_elem_A, prev_elem_B, prev_elem_C = elem_A, elem_B, elem_C
    
    s.wait(1)
    s.next_slide()
    
    s.play(FadeOut(VGroup(
        judul_bab, lbl_A, mat_A, otimes_target, lbl_B, mat_B, 
        eq_target, lbl_C, mat_C, 
        prev_label_i, prev_label_k1, prev_box_row_A,
        prev_label_k2, prev_label_j, prev_box_col_B,
        prev_eq_1, prev_eq_2, prev_eq_3, prev_eq_4,
        prev_label_i_C, prev_label_j_C, prev_box_row_C, prev_box_col_C
    ), shift=LEFT, run_time=1))

def S4_derangement(s):
    check_sym = "✓"
    cross_sym = "✗"
    
    contoh = Tex(r"Contoh Permutasi pada $S_4$", color=BLACK, font_size=32).next_to(title_d, DOWN, buff=0.1)
    perms = list(permutations([1, 2, 3, 4]))
    s.play(Write(contoh), run_time=0.5)

    all_cards = VGroup().next_to(contoh, DOWN, buff=0.5)
    card_data = [] 

    def create_card(p):
        card_bg = RoundedRectangle(corner_radius=0.1, width=2.2, height=0.8, fill_color=WHITE, fill_opacity=1, stroke_color=GRAY, stroke_width=1)
        card_bg.set_z_index(0) 
        slots = VGroup()
        fixed_indices = []
        
        for i, val in enumerate(p):
            sq = Square(side_length=0.4, fill_color=WHITE, fill_opacity=0, stroke_width=0)
            num = Text(str(val), font_size=24, color=BLACK).move_to(sq)
            is_fixed = (val == i + 1)
            if is_fixed:
                fixed_indices.append(i)
            
            idx_lbl = Text(str(i+1), font_size=10, color=GRAY).next_to(sq, DOWN, buff=0.05)
            
            slot_group = VGroup(sq, num, idx_lbl)
            slots.add(slot_group)
        
        slots.arrange(RIGHT, buff=0.15).move_to(card_bg)
        slots.set_z_index(2)
        
        full_card = VGroup(card_bg, slots)
        return full_card, fixed_indices, slots
    
    for p in perms:
        card_obj, fixed_idxs, slots_ref = create_card(p)
        
        is_derangement = (len(fixed_idxs) == 0)
        
        if is_derangement:
            mark = Text(check_sym, font_size=36, color=GREEN).next_to(card_obj[0], RIGHT, buff=0.1)
        else:
            mark = Text(cross_sym, font_size=36, color=RED).next_to(card_obj[0], RIGHT, buff=0.1)
        
        mark.set_opacity(0)
        card_obj.add(mark)
        all_cards.add(card_obj)
        
        card_data.append({
            "mobject": card_obj,
            "bg": card_obj[0],
            "slots": slots_ref,
            "fixed_idxs": fixed_idxs,
            "is_derangement": is_derangement,
            "mark": mark
        })

    all_cards.arrange_in_grid(rows=6, cols=4, buff=0.3)
    max_h = config.frame_height - 2.5
    max_w = config.frame_width - 1.0
    if all_cards.height > max_h:
        all_cards.scale_to_fit_height(max_h)
    if all_cards.width > max_w:
        all_cards.scale_to_fit_width(max_w)
        
    all_cards.move_to(DOWN * 0.5)
    s.play(LaggedStart(*[GrowFromCenter(c) for c in all_cards], lag_ratio=0.03), run_time=1.5)
    s.wait()
    s.next_slide(loop=True)
    
    anims_bad = []
    for data in card_data:
        if not data["is_derangement"]:
            for idx in data["fixed_idxs"]:
                slot_group = data["slots"][idx] 
                anims_bad.append(
                    slot_group[1].animate.set_color(RED).set_weight(BOLD)
                )
                bg_bad = Square(side_length=0.4, color=RED, fill_opacity=0.2, stroke_opacity=0).move_to(slot_group[0])
                bg_bad.set_z_index(1)
                data["mobject"].add(bg_bad) 
            
            anims_bad.append(data["mark"].animate.set_opacity(1))

    s.play(AnimationGroup(*anims_bad, lag_ratio=0.01), run_time=1.5)
    s.wait(0.5)
    
    anims_dim = []
    good_cards = VGroup()
    bad_cards = VGroup()
    for data in card_data:
        if not data["is_derangement"]:
            anims_dim.append(data["mobject"].animate.set_opacity(0.2))
            bad_cards.add(data["mobject"])
        else:
            anims_dim.append(data["bg"].animate.set_stroke(GREEN, width=4))
            anims_dim.append(data["mark"].animate.set_opacity(1))
            good_cards.add(data["mobject"])
            
    s.play(AnimationGroup(*anims_dim), run_time=1)
    s.wait(0.5)
    s.next_slide()
    
    s.play(
        FadeOut(bad_cards),
        run_time=1
    )
    s.play(
        good_cards.animate.arrange_in_grid(rows=3, cols=3, buff=0.5).scale(1.2).move_to(ORIGIN), Unwrite(contoh),
        run_time=1
    )
    final_lbl = Text("Total: 9 Derangement", color=GREEN_E, font_size=32).next_to(good_cards, DOWN, buff=0.5)
    final_box = SurroundingRectangle(good_cards, color=GREEN, buff=0.3, corner_radius=0.2)    
    s.play(Write(final_lbl), Create(final_box), run_time=0.5)
    s.wait()
    s.next_slide()
    s.play(FadeOut(VGroup(good_cards, final_lbl, final_box, title_d), shift=LEFT), run_time=0.5)

def derangement(s):
    COL_TEXT = BLACK
    COL_SLOT = DARK_GRAY
    COL_ITEM = BLUE
    COL_CORRECT = RED   
    COL_WRONG = GREEN   
        
    isi_def = r"""Suatu permutasi $\sigma \in S_n$ disebut \emph{derangement} apabila $\sigma$ tidak memiliki titik tetap, yaitu
            \[
            \sigma(i) \neq i \quad \text{untuk semua } i \in \{1,2,\ldots,n\}.
            \] """
    definisi = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + isi_def + "}", color=COL_TEXT, font_size=30)
    definisi.next_to(title_d, DOWN)
    
    isi_desc = r"""\textit{Derangement} adalah sebuah permutasi dari $n$ objek di mana tidak ada objek yang berada pada posisi aslinya.
    Dalam kehidupan nyata, konsep derangement dapat diterapkan pada berbagai situasi, seperti dalam permainan tukar kado
    di mana setiap peserta harus menerima kado dari orang lain tanpa menerima kado dari dirinya sendiri
    """
    deskripsi = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + isi_desc + "}", color=BLACK, font_size=30)
    deskripsi.next_to(title_d, DOWN)
    s.play(Write(title_d), Write(definisi), run_time=1)
    s.wait(1)
    s.next_slide(auto_next=True)
    s.play(ReplacementTransform(definisi, deskripsi), run_time=1)
    
    n = 4
    slots = VGroup().next_to(deskripsi, DOWN, buff=1.5)
    items = VGroup()
    
    for i in range(n):
        slot_box = Square(side_length=1.2, color=COL_SLOT, stroke_width=2)
        label = Integer(i+1, color=COL_SLOT).move_to(slot_box.get_top() + UP*0.3)
        slot_group = VGroup(slot_box, label)
        slots.add(slot_group)
        
        item_circ = Circle(radius=0.4, color=COL_ITEM, fill_opacity=0.5, fill_color=COL_ITEM)
        item_lbl = Integer(i+1, color=WHITE).move_to(item_circ).set_z_index(3)
        item_group = VGroup(item_circ, item_lbl)
        items.add(item_group)

    slots.arrange(RIGHT, buff=0.5)
    
    for i, item in enumerate(items):
        item.next_to(slots[i], DOWN, buff=0.5)

    s.play(Create(slots), FadeIn(items), run_time=1)
    s.wait(1)
    s.next_slide(loop=True)

    def move_items(permutation, is_derangement):
        anims = []
        targets = []
        for item_idx, slot_idx in enumerate(permutation):
            item = items[item_idx]
            target_slot = slots[slot_idx][0] 
            targets.append(target_slot)
            anims.append(item.animate.move_to(target_slot.get_center()))
        
        lbl_status = Text("Derangement?", color=COL_TEXT, font_size=36).next_to(slots, DOWN, buff=0.5)
        
        s.play(*anims, run_time=1)
    
        highlights = [] 
        highlight_anims = [] 
        
        for i, slot_idx in enumerate(permutation):
            item = items[i]
            rect = SurroundingRectangle(slots[slot_idx], buff=0.1, stroke_width=4)
            
            if i == slot_idx:
                rect.set_color(COL_CORRECT) 
                item.set_color(COL_CORRECT)
            else: 
                rect.set_color(COL_WRONG) 
                item.set_color(COL_WRONG)
            
            highlights.append(rect)          
            highlight_anims.append(Create(rect)) 

        s.play(*highlight_anims, Write(lbl_status), run_time=0.5)
        
        result_text = "Yes" if is_derangement else "No"
        col_res = COL_WRONG if is_derangement else COL_CORRECT
        
        lbl_res = Text(result_text, color=col_res, font_size=28, weight=BOLD).next_to(lbl_status, RIGHT, buff=0.2)
        s.play(Write(lbl_res), run_time=0.5)
        s.wait(0.5)

        reset_anims = []
        for i, item in enumerate(items):
            item.set_color(COL_ITEM) 
            reset_anims.append(item.animate.next_to(slots[i], DOWN, buff=0.5))
        
        s.play(
            *reset_anims, 
            FadeOut(lbl_status), 
            FadeOut(lbl_res),    
            *[FadeOut(h) for h in highlights], 
            run_time=0.8
        )

    move_items([0, 1, 2, 3], False)
    move_items([1, 0, 2, 3], False)
    move_items([1, 0, 3, 2], True)
    move_items([1, 2, 3, 0], True)
    
    s.next_slide()
    s.play(FadeOut(VGroup(slots, items, deskripsi), shift=LEFT), run_time=0.5)

def teorema_matriks(s):
    def text_container(text, font_size=26, color=BLACK):
        return Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + text + "}", color=color, font_size=font_size)
    
    definisi_1 = text_container(r"""\textbf{Definisi 1}.(Matriks LdlP)\\Untuk setiap bilangan real $r \leq 0$ dan bilangan real $k \geq 0$, kita definisikan
                            $[2r, r]_{n}^{k}$ sebagai himpunan matriks $A_{n\times n}$ sedemikian sehingga $a_{ii} = k$ 
                           untuk semua $i$ dan $a_{ij} \in [2r, r]$ untuk $i \neq j$.
                            """)
    teorema_1 = text_container(r""" \textbf{Teorema 1}.\\Misalkan $A \in [2r, r]_{n}^{k_{1}}, \, B \in [2s, s]_{n}^{k_{2}}$ untuk setiap $r, s \leq 0$
                            dan $a_{ii} = k_{1} \geq 0, \, b_{ii} = k_{2} \geq 0$. Maka
                            \[
                              A \otimes B = B \otimes A = k_{2} \otimes A \oplus k_{1} \otimes B.
                            \]""")
    definisi_2 = text_container(r"""\textbf{Definisi 2}.(Matriks Sirkulan)\\ Matriks $A = (a_{ij})$ berukuran $n \times n$ disebut matriks sirkulan jika
                            $a_{ij} = a_{(j-i)\bmod n}$ untuk setiap $1 \leq i, j \leq n$.
                            """)
    teorema_2 = text_container(r"""\textbf{Teorema 2}.\\ Misalkan $A$ dan $B$ adalah matriks sirkulan berukuran $n \times n$, maka $A$ dan $B$ saling komutatif terhadap $\otimes$ yaitu $A \otimes B = B \otimes A$.
                            """)
    deskripsi_full = VGroup(definisi_1, teorema_1, definisi_2, teorema_2).arrange(DOWN, buff=0.4)
    deskripsi_full.next_to(judul_bab, DOWN, buff=0.5)
    s.play(Write(deskripsi_full), run_time=2)
    s.wait()
    s.next_slide()
    s.play(FadeOut(deskripsi_full, judul_bab, shift=LEFT), run_time=1)
    
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
                                       buff=0.3).set_z_index(-1)

    deskripsi_full = VGroup(kalimat, rumus).arrange(DOWN, buff=0.5)
    deskripsi_full.next_to(judul_bab, DOWN, buff=0.5)

    s.play(Write(deskripsi_full), run_time=1)
    s.wait(1)
    s.next_slide()

    s.play(
        FadeOut(kalimat, shift=UP),                
        rumus.animate.next_to(judul_bab, DOWN, buff=0.5), 
        run_time=1.5
    )
    
    rumus_3.next_to(rumus_1, RIGHT, buff=0.1) 
    kotak_rumus.move_to(rumus.get_center())
    
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
    group_a = VGroup(label_a, mat_a.scale(0.6)).arrange(RIGHT, buff=0.2)
    group_b = VGroup(label_b, mat_b.scale(0.6)).arrange(RIGHT, buff=0.2)

    s.play(VGroup(rumus_1,rumus_3, kotak_rumus).animate.to_edge(LEFT, buff=1.5), run_time=0.5)

    group_a.next_to(rumus_3, RIGHT, buff=1.5)
    group_b.next_to(group_a, RIGHT, buff=0.5)
    kotak_group_a_b = SurroundingRectangle(
        VGroup(group_a, group_b),
        color=GREEN_D,
        fill_color=GREEN_D,
        fill_opacity=0.6,
        corner_radius=0,
        buff=0.2
    ).set_z_index(-1)

    s.play(Write(group_a), Write(group_b), Write(kotak_group_a_b), run_time=0.5)
    s.wait(1)
    s.next_slide(auto_next=True)

    target_mat_a = mat_a.copy().scale(2)
    target_mat_b = mat_b.copy().scale(2)

    target_mat_res = mat_res.copy()
    target_mat_res.get_entries().set_opacity(0)
    target_mat_res.get_brackets().set_color(BLACK)

    times_sym = MathTex(r"\otimes", font_size=60, color=BLACK)
    equals_sym = MathTex(r"=", font_size=60, color=BLACK)

    big_A = MathTex("A", font_size=60, color=BLACK)
    big_B = MathTex("B", font_size=60, color=BLACK)

    group_awal = VGroup(big_A, times_sym, big_B, equals_sym, target_mat_res)
    group_awal.arrange(RIGHT, buff=0.5)
    group_awal.move_to(DOWN * 1)

    target_mat_res.match_height(target_mat_a)

    group_akhir = VGroup(
        target_mat_a, 
        times_sym.copy(),
        target_mat_b, 
        equals_sym.copy(), 
        target_mat_res.copy()
    )
    group_akhir.arrange(RIGHT, buff=0.3)
    group_akhir.move_to(DOWN * 1)

    s.play(Write(group_awal), run_time=1)
    s.wait(0.5)

    s.play(
        ReplacementTransform(group_awal, group_akhir),
        run_time=1.5
    )
    s.wait(0.5)
    
    final_mat_a = group_akhir[0]
    final_mat_b = group_akhir[2]
    final_mat_res = group_akhir[4]

    s.next_slide(loop=True)

    for r in range(rows_a):
        for c in range(cols_b):
            row_obj = final_mat_a.get_rows()[r]
            col_obj = final_mat_b.get_columns()[c]
            
            rect_row = SurroundingRectangle(row_obj, color=BLUE, buff=0.1)
            rect_col = SurroundingRectangle(col_obj, color=GREEN, buff=0.1)
            
            s.play(Create(rect_row), Create(rect_col), run_time=0.5)

            parts_str = []
            sums_val = []
            for k in range(cols_a):
                val_a = matrix_A[r][k]
                val_b = matrix_B[k][c]
                val_sum = val_a + val_b
                sums_val.append(val_sum)
                parts_str.append(f"({val_a}+{val_b})")
            
            max_val = max(sums_val)
            inner_content = ", ".join(parts_str)

            latex_str = f"\\max \\big( {inner_content} \\big) = {max_val}"
            
            step_calculation = MathTex(latex_str, font_size=34, color=DARK_BROWN).next_to(group_akhir, DOWN, buff=0.3)

            s.play(Write(step_calculation), run_time=0.8)
            s.wait(0.5)

            entry_index = r * cols_b + c
            target_entry = final_mat_res.get_entries()[entry_index]

            target_entry.set_value(max_val)

            source_part = step_calculation[-len(str(max_val)):] 
            
            s.play(
                ReplacementTransform(source_part, target_entry),
                target_entry.animate.set_opacity(1),
                run_time=0.8
            )

            s.play(
                FadeOut(rect_row),
                FadeOut(rect_col),
                FadeOut(step_calculation),
                run_time=0.4
            )
    s.play(Indicate(final_mat_res,color=DARK_BROWN, scale_factor=1.1), run_time=1)
    s.wait()
    s.next_slide()
    s.play(FadeOut(VGroup(rumus_1, rumus_3, kotak_rumus, group_akhir,final_mat_res, group_a, group_b, kotak_group_a_b), shift=LEFT))

def aljabar_max_plus(s):
    my_template = TexTemplate()
    my_template.add_to_preamble(r"\usepackage{xcolor}")
    my_template.add_to_preamble(r"\usepackage{amsmath}")
    my_template.add_to_preamble(r"\usepackage{amssymb}")

    singkatnya = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""Aljabar max-plus salah satu cabang dari aljabar tropikal 
                     yang menggunakan operasi maksimum dan penjumlahan sebagai operasi dasar.}""", color=BLACK, font_size=30, tex_template=my_template).next_to(judul_bab, DOWN, buff=0.5)
    
    deskripsi = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{" + r"""
    Aljabar max-plus salah satu cabang dari aljabar tropikal yang menggunakan operasi maksimum dan penjumlahan sebagai operasi dasar. 
    Didefinisikan himpunan $\mathbb{R}_{\max} = \mathbb{R} \cup \{-\infty\}$, $(\mathbb{R}_{\max}, \oplus, \otimes)$ disebut 
    \textit{semiring} max-plus sehingga untuk setiap $a, b \in \mathbb{R}_{\max}$ berlaku
    \begin{align*}
        a \oplus b & = \max(a, b) \\
        a \otimes b & = a + b
    \end{align*}
    Di mana elemen identitasnya adalah $\varepsilon={-\infty}$ untuk operasi $\oplus$ dan $0$ untuk operasi $\otimes$.
    }""", color=BLACK, font_size=30, tex_template=my_template).next_to(judul_bab, DOWN, buff=0.5)

    s.play(Write(judul_bab),Write(singkatnya))
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
