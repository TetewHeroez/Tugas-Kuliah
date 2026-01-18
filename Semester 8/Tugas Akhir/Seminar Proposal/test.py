from manim import *
from lib.slide_tracker import *

config.background_color = WHITE

class RevisionScene(Scene):
    def construct(self):
        latin_square(self)

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
    s.play(FadeOut(VGroup(full_equation, judul_bab, deskripsi_baru, cycle_group), scale=0.5), run_time=1)
    
