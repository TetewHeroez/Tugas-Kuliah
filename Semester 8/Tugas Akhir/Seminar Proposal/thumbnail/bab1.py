from manim import *

config.background_color = "#FFFFFF"

class DiffieHellmanExchange(Scene):
    def construct(self):
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
        self.play(Write(judul), run_time=0.4)

        pos_intro_pub = LEFT * 3
        pos_intro_priv = RIGHT * 3

        intro_pub_key = get_key(YELLOW, pos_intro_pub)
        intro_priv_key = get_key(GRAY, pos_intro_priv)

        lbl_intro_pub = MathTex("\\text{Kunci Publik } (g, p)", color=BLACK).next_to(intro_pub_key, UP)
        lbl_intro_priv = MathTex("\\text{Kunci Privat } (a, b)", color=BLACK).next_to(intro_priv_key, UP)

        self.play(
            DrawBorderThenFill(intro_pub_key), Write(lbl_intro_pub),
            DrawBorderThenFill(intro_priv_key), Write(lbl_intro_priv),
            run_time=0.5
        )
        self.wait(0.4)

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

        self.play(
            ReplacementTransform(lbl_intro_pub,lbl_gp), ReplacementTransform(lbl_intro_priv, VGroup(lbl_a, lbl_b)),
            Write(alice_lbl), Write(bob_lbl),
            ReplacementTransform(intro_pub_key, real_pub_key),
            ReplacementTransform(intro_priv_key, VGroup(real_alice_priv, real_bob_priv)),
            run_time=0.6
        )
        self.wait(0.25)

        copy_pub_alice = real_pub_key.copy().move_to(real_alice_priv.get_center() + UP*1)
        copy_pub_bob = real_pub_key.copy().move_to(real_bob_priv.get_center() + UP*1)

        math_gp_a = MathTex("g", "^{\dots}", "\\pmod{p}", color=BLACK).scale(0.7).next_to(real_alice_priv, DOWN)
        math_gp_b = MathTex("g", "^{\dots}", "\\pmod{p}", color=BLACK).scale(0.7).next_to(real_bob_priv, DOWN)

        self.play(
            TransformFromCopy(real_pub_key, copy_pub_alice),
            TransformFromCopy(real_pub_key, copy_pub_bob),
            GrowFromPoint(math_gp_a,lbl_gp.get_center()), GrowFromPoint(math_gp_b,lbl_gp.get_center()),
            run_time=0.4
        )

        key_A_orange = get_key(ORANGE, real_alice_priv.get_center())
        key_B_green = get_key(GREEN, real_bob_priv.get_center())

        math_A = MathTex("g", "^a", "\\pmod{p}", color=BLACK).scale(0.7).next_to(key_A_orange, DOWN)
        math_B = MathTex("g", "^b", "\\pmod{p}", color=BLACK).scale(0.7).next_to(key_B_green, DOWN)

        self.play(
            TransformMatchingShapes(VGroup(copy_pub_alice, real_alice_priv), key_A_orange),
            TransformMatchingShapes(VGroup(copy_pub_bob, real_bob_priv), key_B_green),
            FadeOut(math_gp_a[1]), FadeOut(math_gp_b[1]), 
            ReplacementTransform(lbl_a.copy(),math_A[1]), 
            ReplacementTransform(lbl_b.copy(),math_B[1]),
            ReplacementTransform(math_gp_a[0], math_A[0]),
            ReplacementTransform(math_gp_a[2], math_A[2]),
            ReplacementTransform(math_gp_b[0], math_B[0]),
            ReplacementTransform(math_gp_b[2], math_B[2]),
            lag_ratio=0.5,
            run_time=0.4
        )
        self.wait(0.25)

        loc_alice = key_A_orange.get_center()
        loc_bob = key_B_green.get_center()

        self.play(
            key_A_orange.animate.move_to(loc_bob),
            key_B_green.animate.move_to(loc_alice),
            math_A.animate.next_to(loc_bob, DOWN*2.5), 
            math_B.animate.next_to(loc_alice, DOWN*2.5),
            path_arc=PI/1.2,
            run_time=0.6
        )
        self.wait(0.15)

        sec_a = get_key(RED, key_B_green.get_center()+ UP * 1.0).set_opacity(0.8)
        sec_b = get_key(BLUE, key_A_orange.get_center()+ UP * 1.0).set_opacity(0.8)

        self.play(GrowFromPoint(sec_a, lbl_a.get_center()), GrowFromPoint(sec_b, lbl_b.get_center()), run_time=0.25)

        shared_alice = get_key(GOLD_E, key_B_green.get_center())
        shared_bob = get_key(GOLD_E, key_A_orange.get_center())

        math_A_shared = MathTex("(g", "^b)^a", "\\pmod{p}", color=BLACK).scale(0.7).next_to(shared_alice, DOWN)
        math_B_shared = MathTex("(g", "^a)^b", "\\pmod{p}", color=BLACK).scale(0.7).next_to(shared_bob, DOWN)

        self.play(
            TransformMatchingShapes(VGroup(key_B_green, sec_a), shared_alice),
            TransformMatchingShapes(VGroup(key_A_orange, sec_b), shared_bob),
            FadeOut(math_A[1]), FadeOut(math_B[1]), 
            ReplacementTransform(lbl_a.copy(),math_A_shared[1]), 
            ReplacementTransform(lbl_b.copy(),math_B_shared[1]),
            ReplacementTransform(math_A[0], math_B_shared[0]),
            ReplacementTransform(math_A[2], math_B_shared[2]),
            ReplacementTransform(math_B[0], math_A_shared[0]),
            ReplacementTransform(math_B[2], math_A_shared[2]),
            lag_ratio=0.5,
            run_time=0.4
        )

        final_center_key = get_key(GOLD_E,ORIGIN+UP, scale=0.6)
        
        final_lbl = MathTex("\\text{Kunci Bersama}", color=BLACK).next_to(final_center_key, UP)

        eq = MathTex("=", color=DARK_BROWN).next_to(final_center_key, DOWN*3)
        rhs_eq = MathTex("g^{ba}\\pmod{p}", color=DARK_BROWN    ).next_to(eq, RIGHT)
        lhs_eq = MathTex("g^{ab}\\pmod{p}", color=DARK_BROWN).next_to(eq, LEFT)
        box = SurroundingRectangle(VGroup(eq, lhs_eq, rhs_eq), color=DARK_BROWN , buff=0.2, stroke_width=2)

        self.play(
            FadeOut(alice_lbl), FadeOut(bob_lbl), FadeOut(lbl_a), FadeOut(lbl_b), 
            FadeOut(lbl_gp), FadeOut(real_pub_key),
            ReplacementTransform(shared_alice, final_center_key),
            ReplacementTransform(shared_bob, final_center_key),
            Transform(math_A_shared, lhs_eq),
            Transform(math_B_shared, rhs_eq),
            run_time=0.5
        )

        self.play(Write(final_lbl),
            Write(eq),
            Write(box),
            run_time=0.5
        )

        self.play(Indicate(final_lbl, color=YELLOW), Circumscribe(VGroup(eq, lhs_eq, rhs_eq), buff=0.2), run_time=0.5)