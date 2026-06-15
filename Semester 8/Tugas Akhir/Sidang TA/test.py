from manim import *
from lib.slide_tracker import *

config.background_color = WHITE

class RevisionScene(Scene):
    def construct(self):
        permutasi(self)

def permutasi(s):
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
    # matrix_mobj.next_to(deskripsi_baru, DOWN, buff=1)
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
    # s.next_slide(loop=True)
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