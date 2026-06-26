from manim import *
from manim_slides import Slide
from lib.slide_tracker import *

config.background_color = WHITE

class RevisionScene(Slide):
    def construct(self):
        SyaratPerlu(self)

def SyaratPerlu(s):
    s.next_slide()
    Mobject.set_default(color=BLACK)
    judul = Title("Akibat: Konjugasi Menjaga Komutatif", color=BLACK, font_size=40, include_underline=True)
    judul[-1].set_color(BLACK)
    
    deskripsi = Tex(
        r"\parbox{" + str(config.frame_width) + r"cm}{"
        r"\texbf{Akibat 1.} Misalkan $A,B\in L_S(n)$ dan misalkan $P_\rho$ adalah matriks permutasi max-plus yang bersesuaian dengan permutasi $\rho\in S_n$. Jika $A\otimes B=B\otimes A$, maka}",
        color=BLACK, font_size=30
    ).next_to(judul, DOWN, buff=0.4)
    
    s.play(Write(judul))
    s.play(Write(deskripsi), run_time=1.5)
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

    s.play(Write(full_eq), run_time=2)
    s.wait(1)
    s.next_slide()

    eq1 = MathTex(
        r"(", r"P_\rho^{-1}", r"\otimes", "A", r"\otimes", r"P_\rho", r")",
        r"\otimes",
        r"(", r"P_\rho^{-1}", r"\otimes", "B", r"\otimes", r"P_\rho", r")",
        font_size=42
    )
    eq1[3].set_color(PURE_BLUE)
    eq1[11].set_color(PURE_RED)
    eq1.next_to(full_eq, DOWN, buff=0.8)
    
    s.play(ReplacementTransform(full_eq[0:15].copy(), eq1), run_time=1.5)
    s.wait(1)
    s.next_slide()

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
    s.next_slide()

    box = SurroundingRectangle(eq2[4:7], color=GREEN_E, buff=0.1)
    s.play(Create(box))
    ident = MathTex("I", color=GREEN_E, font_size=42).move_to(box)
    s.play(ReplacementTransform(eq2[4:7], ident), FadeOut(box))
    s.wait(0.5)

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
    s.wait(1)
    s.next_slide()

    box2 = SurroundingRectangle(eq3[2:5], color=DARK_GRAY, buff=0.1)
    s.play(Create(box2))
    
    asumsi_popup = MathTex("A", r"\otimes", "B", "=", "B", r"\otimes", "A", color=BLACK, font_size=36)
    asumsi_popup[0].set_color(PURE_BLUE)
    asumsi_popup[2].set_color(PURE_RED)
    asumsi_popup[4].set_color(PURE_RED)
    asumsi_popup[6].set_color(PURE_BLUE)
    asumsi_popup.next_to(box2, UP, buff=0.3)
    
    s.play(FadeIn(asumsi_popup, shift=DOWN))
    s.wait(1)
    
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
        run_time=1.5
    )
    s.remove(*eq3)
    s.add(eq4)
    s.wait(0.5)
    s.play(FadeOut(box2), FadeOut(asumsi_popup, shift=UP))
    s.wait(0.5)
    s.next_slide()

    ident2 = MathTex("I", color=GREEN_E, font_size=42).move_to(eq4[3])
    s.play(
        eq4[0:3].animate.shift(LEFT*1.2),
        eq4[4:7].animate.shift(RIGHT*1.2),
        FadeIn(ident2, scale=0)
    )
    s.wait(0.5)

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
    s.next_slide()

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
    
    s.wait(1)
    s.next_slide()
    
    # "Substitusi ke sisi kanan" -> terbang dan gabung ke RHS
    s.play(
        eq6.animate.scale(32/42).move_to(full_eq[16:31]),
        run_time=1.5
    )
    box_rhs = SurroundingRectangle(full_eq, color=BLACK, buff=0.1)
    s.play(FadeIn(box_rhs))
    s.play(FadeOut(eq6))
    
    s.wait(2)
    s.next_slide()
    
    s.play(*[FadeOut(m) for m in s.mobjects])
    