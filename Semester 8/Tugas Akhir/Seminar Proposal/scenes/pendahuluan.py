from manim import *
from scenes.content import *

def pendahuluan(s):
#   diffie_hellman(s)
  stickel_protocol(s)
   
def stickel_protocol(s):
    judul_stickel = Title("Protokol Stickel (E. Stickel, 2005)", color=BLACK, font_size=48)
    judul_stickel[-1].set_color(BLACK)
    
    lebar_teks = f"{config.frame_width - 1}cm" 
    my_template = TexTemplate()
    my_template.add_to_preamble(r"\usepackage{enumitem}")
    my_template.add_to_preamble(r"\usepackage{amssymb}")

    isi_stickel = r"""
        Misalkan $G$ adalah grup non-abelian hingga, dan $a, b \in G$ dengan $ab \neq ba$.
        \begin{itemize}[label=$\bullet$, leftmargin=0.5cm]
            \item Bob memilih $r, s \in \mathbb{N}$, kemudian mengirimkan $c = a^{r} b^{s}$ kepada Alice.
            \item Alice memilih $v, w \in \mathbb{N}$, kemudian mengirimkan $d = a^{v} b^{w}$ kepada Bob.
            \item Alice menghitung kunci bersama $k= a^v c b^w$.
            \item Bob dengan cara yang sama menghitung $k = a^r d b^s$. 
        \end{itemize}
        """

    algoritma_stickel = Tex(
            r"\parbox{" + lebar_teks + r"}{" + isi_stickel + r"}", 
            font_size=30,
            color=BLACK,
            tex_template=my_template
        ).to_edge(LEFT, buff=1)
    
    lebar_setengah = f"{config.frame_width / 2 }cm"
    algoritma_stickel_col = Tex(
            r"\parbox{" + lebar_setengah + r"}{" + isi_stickel + r"}", 
            font_size=30, 
            color=BLACK,
            tex_template=my_template
        ).to_edge(LEFT, buff=0.5)
    algoritma_tropikal = Tex(
        r"\parbox{" + lebar_setengah + r"}{"
        r"""
        Misalkan matriks $W \in \mathbb{R}_{\max}^{n \times n}$.
        \begin{itemize}[label=$\bullet$, leftmargin=0.5cm, itemsep=0.3cm]
            \item Alice memilih matriks acak $A_1, A_2$, kemudian mengirimkan
            $U = A_1 \otimes W \otimes A_2$ kepada Bob.
            \item Bob memilih matriks acak $B_1, B_2$, kemudian mengirimkan
            $V = B_1 \otimes W \otimes B_2$ kepada Alice.
            \item Alice menghitung kunci bersama $K = A_1 \otimes V \otimes A_2$.
            \item Bob dengan cara yang sama menghitung $K = B_1 \otimes U \otimes B_2$.
        \end{itemize}
        """
        r"}",
        font_size=30,
        color=BLACK,
        tex_template=my_template
    ).to_edge(RIGHT, buff=0.5).shift(DOWN*0.45)

    # judul.next_to(algoritma, UP, buff=0.5)
    s.play(Write(judul_stickel))
    # s.play(judul_stickel[1].animate.match_width(judul_stickel[0]))
    s.play(Write(algoritma_stickel), run_time=2)
    s.wait()
    s.next_slide()

    garis_tengah = Line(UP*5, DOWN*5, color=DARK_GRAY).next_to(algoritma_stickel_col, RIGHT, buff=0.5)
    target_teks = judul_stickel[0].copy()
    target_teks.move_to(algoritma_stickel_col.get_top()+UP)
    target_teks.set_width(algoritma_stickel_col.width * 0.8)
    judul_stickel_bg = SurroundingRectangle(
            target_teks,
            color=BLUE_D,
            fill_color=BLUE_B,
            fill_opacity=0.5,
            corner_radius=0.2,
            buff=0.2,
            stroke_width=2
        )
    judul_tropikal = Tex("Protokol Tropikal", font_size=target_teks.font_size, color=BLACK)
    judul_tropikal.set_text("Protokol Tropikal")
    judul_tropikal.move_to(algoritma_tropikal.get_top()+UP)
    judul_tropikal_bg = SurroundingRectangle(
            judul_tropikal,
            color=GREEN_D,
            fill_color=GREEN_B,
            fill_opacity=0.5,
            corner_radius=0.2,
            buff=0.2,
            stroke_width=2
        )   


    s.play(
       ReplacementTransform(algoritma_stickel, algoritma_stickel_col),
       Create(garis_tengah),
       Write(algoritma_tropikal),
       Transform(judul_stickel[1], judul_stickel_bg),
       Transform(judul_stickel[0], target_teks),
        Write(judul_tropikal_bg),
        Write(judul_tropikal),
       run_time=2
    )
    s.wait()
    
    s.next_slide()

def diffie_hellman(s):
   def get_key(color, location, scale=0.4):
       blade = VMobject()
       blade.set_points_as_corners([
           [-1.5, 0, 0], [2.5, 0, 0], [2.5, -0.5, 0], [2, -0.5, 0], [2, -1, 0],
           [1.5, -1, 0], [1.5, -0.5, 0], [1, -0.5, 0], [1, -1, 0], [0.5, -1, 0],
           [0.5, -0.5, 0], [-1.5, -0.5, 0], [-1.5, 0, 0]
       ])
       blade.set_fill(color, opacity=1)
       blade.set_stroke(width=3, color=BLACK)
       ring = Annulus(inner_radius=0.4, outer_radius=0.8, color=BLACK, stroke_width=3)
       ring.set_fill(color, opacity=1)
       ring.move_to([-2, -0.25, 0])
       whole_key = VGroup(blade, ring)
       whole_key.scale(scale)
       whole_key.move_to(location)
       return whole_key
   
   judul = Title("Pertukaran Kunci Diffie-Hellman", color=BLACK, font_size=48)
   judul[-1].set_color(BLACK) 
 
   lebar_teks = f"{config.frame_width - 2}cm"
   deskripsi = Tex(
            r"\parbox{" + lebar_teks + r"}{"
            r"\textbf{Protokol pertukaran kunci kriptografi} "
            r"yang memungkinkan dua pihak membentuk kunci rahasia bersama melalui saluran "
            r"komunikasi publik, tanpa pernah mengirimkan kunci rahasia tersebut secara langsung."
            r"}",
            font_size=34,
            color=BLACK  
        )
   
   deskripsi.next_to(judul, DOWN, buff=0.5)

   pos_intro_pub = LEFT * 3
   pos_intro_priv = RIGHT * 3
   # Objek Kunci Intro
   intro_pub_key = get_key(YELLOW, pos_intro_pub)
   intro_priv_key = get_key(GRAY, pos_intro_priv)
   # Label Variabel
   lbl_intro_pub = MathTex("\\text{Kunci Publik } (g, p)", color=BLACK).next_to(intro_pub_key, DOWN)
   lbl_intro_priv = MathTex("\\text{Kunci Privat } (a, b)", color=BLACK).next_to(intro_priv_key, DOWN)
   # Animasi Intro
   s.play(
       Write(judul),
       Write(deskripsi, run_time=1.5),
       DrawBorderThenFill(intro_pub_key), Write(lbl_intro_pub),
       DrawBorderThenFill(intro_priv_key), Write(lbl_intro_priv),
       lag_ratio=0.5,
       run_time=1
   )
   s.wait()

   s.next_slide() 

   alice_lbl = MathTex("\\text{Alice}", color=RED).scale(1.5).to_corner(DL, buff=1.5)
   bob_lbl = MathTex("\\text{Bob}", color=BLUE).scale(1.5).to_corner(DR, buff=1.5)

   target_pub_loc = UP * 1.2
   target_alice_priv_loc = alice_lbl.get_center() + UP * 1.5 + RIGHT * 1
   target_bob_priv_loc = bob_lbl.get_center() + UP * 1.5 + LEFT * 1

   real_pub_key = get_key(YELLOW, target_pub_loc)
   real_alice_priv = get_key(RED, target_alice_priv_loc)
   real_bob_priv = get_key(BLUE, target_bob_priv_loc)

   lbl_gp = MathTex("g, p", color=BLACK).next_to(real_pub_key, UP)
   lbl_a = MathTex("a", color=RED).next_to(real_alice_priv, 1.1*LEFT )
   lbl_b = MathTex("b", color=BLUE).next_to(real_bob_priv, 1.1*RIGHT )

   s.play(
       Unwrite(deskripsi,run_time=0.5),
       ReplacementTransform(lbl_intro_pub, lbl_gp), ReplacementTransform(lbl_intro_priv, VGroup(lbl_a, lbl_b)),
       Write(alice_lbl), Write(bob_lbl),
       ReplacementTransform(intro_pub_key, real_pub_key),
       ReplacementTransform(intro_priv_key, VGroup(real_alice_priv, real_bob_priv)),
       run_time=1.2
   )
   s.wait()

   s.next_slide()

   copy_pub_alice = real_pub_key.copy().move_to(real_alice_priv.get_center() + UP*1)
   copy_pub_bob = real_pub_key.copy().move_to(real_bob_priv.get_center() + UP*1)

   math_gp_a = MathTex("g", "^{\dots}", "\\pmod{p}", color=BLACK).scale(0.7).next_to(real_alice_priv, DOWN)
   math_gp_b = MathTex("g", "^{\dots}", "\\pmod{p}", color=BLACK).scale(0.7).next_to(real_bob_priv, DOWN)
   s.play(
       TransformFromCopy(real_pub_key, copy_pub_alice),
       TransformFromCopy(real_pub_key, copy_pub_bob),
       GrowFromPoint(math_gp_a, lbl_gp.get_center()), GrowFromPoint(math_gp_b, lbl_gp.get_center()),
       run_time=0.8
   )
   s.wait()
   s.next_slide() 

   key_A_orange = get_key(ORANGE, real_alice_priv.get_center())
   key_B_green = get_key(GREEN, real_bob_priv.get_center())
   math_A = MathTex("g", "^a", "\\pmod{p}", color=BLACK).scale(0.7).next_to(key_A_orange, DOWN)
   math_B = MathTex("g", "^b", "\\pmod{p}", color=BLACK).scale(0.7).next_to(key_B_green, DOWN)
   s.play(
       TransformMatchingShapes(VGroup(copy_pub_alice, real_alice_priv), key_A_orange),
       TransformMatchingShapes(VGroup(copy_pub_bob, real_bob_priv), key_B_green),
       FadeOut(math_gp_a[1]), FadeOut(math_gp_b[1]), 
       ReplacementTransform(lbl_a.copy(), math_A[1]), 
       ReplacementTransform(lbl_b.copy(), math_B[1]),
       ReplacementTransform(math_gp_a[0], math_A[0]), ReplacementTransform(math_gp_a[2], math_A[2]),
       ReplacementTransform(math_gp_b[0], math_B[0]), ReplacementTransform(math_gp_b[2], math_B[2]),
       lag_ratio=0.5,
       run_time=0.8
   )
   s.wait()

   s.next_slide()

   loc_alice = key_A_orange.get_center()
   loc_bob = key_B_green.get_center()
   s.play(
       key_A_orange.animate.move_to(loc_bob),
       key_B_green.animate.move_to(loc_alice),
       math_A.animate.next_to(loc_bob, DOWN*2.5), 
       math_B.animate.next_to(loc_alice, DOWN*2.5),
       path_arc=PI/1.2,
       run_time=1.2
   )
   s.wait()
   
   s.next_slide()

   sec_a = get_key(RED, key_B_green.get_center()+ UP * 1.0)
   sec_b = get_key(BLUE, key_A_orange.get_center()+ UP * 1.0)
   s.play(GrowFromPoint(sec_a, lbl_a.get_center()), GrowFromPoint(sec_b, lbl_b.get_center()), run_time=0.5)
   s.wait()
   s.next_slide() 
   shared_alice = get_key(GOLD_E, key_B_green.get_center())
   shared_bob = get_key(GOLD_E, key_A_orange.get_center())
   math_A_shared = MathTex("(g", "^b)^a", "\\pmod{p}", color=BLACK).scale(0.7).next_to(shared_alice, DOWN)
   math_B_shared = MathTex("(g", "^a)^b", "\\pmod{p}", color=BLACK).scale(0.7).next_to(shared_bob, DOWN)
   s.play(
       TransformMatchingShapes(VGroup(key_B_green, sec_a), shared_alice),
       TransformMatchingShapes(VGroup(key_A_orange, sec_b), shared_bob),
       FadeOut(math_A[1]), FadeOut(math_B[1]), 
       ReplacementTransform(lbl_a.copy(), math_A_shared[1]), 
       ReplacementTransform(lbl_b.copy(), math_B_shared[1]),
       ReplacementTransform(math_A[0], math_B_shared[0]), 
       ReplacementTransform(math_A[2], math_B_shared[2]),
       ReplacementTransform(math_B[0], math_A_shared[0]), 
       ReplacementTransform(math_B[2], math_A_shared[2]),
       run_time=1.5
   )
   s.wait()
   s.next_slide()
   math_A_shared_2 = MathTex("g", "^{ba}", "\\pmod{p}", color=BLACK).scale(0.7).next_to(shared_alice, DOWN)
   math_B_shared_2 = MathTex("g", "^{ab}", "\\pmod{p}", color=BLACK).scale(0.7).next_to(shared_bob, DOWN)
   because = Tex("\\text{*karena } ab = ba", font_size=24).set_color(BLACK).next_to(ORIGIN, DOWN*5)
   s.play(
         TransformMatchingShapes(math_A_shared, math_A_shared_2),
         TransformMatchingShapes(math_B_shared, math_B_shared_2),
         Write(because),
         run_time=1.0
   )

   final_center_key = get_key(GOLD_E, ORIGIN+UP, scale=0.6)
   final_lbl = MathTex("\\text{Kunci Bersama}", color=BLACK).next_to(final_center_key, UP)

   s.next_slide()
   eq = MathTex("=", color=DARK_BROWN).next_to(final_center_key, DOWN*3)
   rhs_eq = MathTex("g^{ab}\\pmod{p}", color=DARK_BROWN).next_to(eq, RIGHT)
   lhs_eq = MathTex("g^{ba}\\pmod{p}", color=DARK_BROWN).next_to(eq, LEFT)
   box = SurroundingRectangle(VGroup(eq, lhs_eq, rhs_eq), color=DARK_BROWN, buff=0.2, stroke_width=2)
   s.play(
       FadeOut(alice_lbl), FadeOut(bob_lbl), FadeOut(lbl_a), FadeOut(lbl_b), 
       FadeOut(lbl_gp), FadeOut(real_pub_key),
       ReplacementTransform(shared_alice, final_center_key),
       ReplacementTransform(shared_bob, final_center_key),
       Transform(math_A_shared_2, lhs_eq),
       Transform(math_B_shared_2, rhs_eq),
   )
   s.play(Write(final_lbl), Write(eq), Write(box))
   s.play(Indicate(final_lbl, color=YELLOW), Circumscribe(VGroup(eq, lhs_eq, rhs_eq), buff=0.2))
   s.wait()

   summary = MathTex("\\therefore","\\text{Sifat komutatif dan asosiatif perkalian diperlukan}", font_size=36).set_color(BLACK).next_to(because, DOWN*2)
   s.next_slide()
   s.play(Transform(because,summary))
   s.wait()
  

   s.next_slide()
   s.play(Unwrite(because), Unwrite(final_center_key),Unwrite(final_lbl), Unwrite(box), Unwrite(VGroup(eq, math_A_shared_2, math_B_shared_2)), Unwrite(judul), run_time=1)

   
   
#    s.play(*[FadeOut(mobj) for mobj in s.mobjects])