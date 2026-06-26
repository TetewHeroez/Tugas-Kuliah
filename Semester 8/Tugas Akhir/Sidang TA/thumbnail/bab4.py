from manim import *

config.background_color = WHITE

class Bab4Thumbnail(Scene):
    def construct(self):
        speed = 0.5
        s = self
        Mobject.set_default(color=BLACK)
        judul = Title("Himpunan Superlevel", color=BLACK, font_size=48, include_underline=True)
        judul[-1].set_color(BLACK)
        
        deskripsi = Tex(
            r"\parbox{" + str(config.frame_width) + r"cm}{"
            r"\textbf{Definisi 5.} Himpunan superlevel dari hasil perkalian $A\otimes B$ pada level $v$, yang dinotasikan dengan $\mathcal{U}_{\ge v}^{AB}$, didefinisikan sebagai \[\mathcal{U}_{\ge v}^{AB}=\bigcup_{\substack{x,y\in \underline{n}\\x+y\ge v}}\Gamma(\sigma_y^B\circ\sigma_x^A).\]}", 
            color=BLACK, font_size=30).next_to(judul, DOWN, buff=0.2)
        s.play(Write(judul), Write(deskripsi), run_time=1 * speed)
        s.wait(1 * speed)
        
        mat_A = Matrix([["1","2","3","4","5"],["2","1","4","5","3"],["3","5","1","2","4"],["4","3","5","1","2"],["5","4","2","3","1"]], v_buff=0.6, h_buff=0.8).scale(0.55).set_color(BLACK)
        mat_B = Matrix([["1","2","3","4","5"],["2","1","4","5","3"],["3","5","1","2","4"],["4","3","5","1","2"],["5","4","2","3","1"]], v_buff=0.6, h_buff=0.8).scale(0.55).set_color(BLACK)
        
        for ent in mat_A.get_entries(): ent.set_color(BLACK)
        for ent in mat_B.get_entries(): ent.set_color(BLACK)
        
        lbl_A = MathTex("A =").scale(0.7).next_to(mat_A, LEFT)
        lbl_B = MathTex("B =").scale(0.7).next_to(mat_B, LEFT)
        
        grp_A = VGroup(lbl_A, mat_A)
        grp_B = VGroup(lbl_B, mat_B)
        grp_matrices = VGroup(grp_A, grp_B).arrange(RIGHT, buff=1.0).next_to(deskripsi, DOWN, buff=0.5)
        
        s.play(Write(grp_matrices), run_time=1 * speed)
        s.wait(1 * speed)
        
        s.play(grp_A.animate.to_edge(LEFT, buff=0.5).scale(0.6), grp_B.animate.to_edge(LEFT, buff=0.5).shift(DOWN*1.5).scale(0.6), run_time=1 * speed)
        
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
        
        s.play(Write(grp_AB), Create(grid), run_time=1 * speed)
        s.wait(0.5 * speed)
        
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
                    *[f[0].animate.set_fill(opacity=0) for f in grid],
                    run_time=1 * speed
                )
            else:
                s.play(Write(form_tex), run_time=1 * speed)
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
                run_time=1 * speed
            )
            s.wait(1 * speed)
            
            prev_hi = highlights
        
        s.play(FadeOut(VGroup(judul, deskripsi, grp_matrices, grp_AB, grid, prev_hi, prev_form), shift=LEFT), run_time=1 * speed)
