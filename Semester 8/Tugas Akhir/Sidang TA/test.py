from manim import *
from lib.slide_tracker import *

config.background_color = WHITE

class RevisionScene(Scene):
    def construct(self):
        centralizer(self)

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

    s.play(Write(judul), run_time=1)
    s.play(Write(teks_atas), Write(definisi), run_time=1)
    s.play(Write(teks_bawah), Write(teorema), run_time=1)
    s.wait(2)

    # 2. Kemunculan Sigma dan Substitusi Teorema Barengan
    sigma_tex = MathTex(
        r"\sigma =", r"(1\;3\;4)", r"(2\;7\;8)", r"(5\;6\;9)", r"\in S_9",
        color=BLACK, font_size=42
    ).next_to(judul, DOWN, buff=0.5)
    
    # sigma_tex[1].set_color(BLUE_E)     # (1 3 4)
    # sigma_tex[2].set_color(RED_E)      # (2 7 8)
    # sigma_tex[3].set_color(GREEN_E)    # (5 6 9)

    subst_final = MathTex(
        r"C_{S_9}(\sigma) \cong \mathbb{Z}_3^3 \rtimes S_3",
        color=BLACK, font_size=42
    ).next_to(sigma_tex, DOWN, buff=0.8)

    s.play(
        FadeOut(VGroup(teks_atas, definisi, teks_bawah)),
        Write(sigma_tex),
        Transform(teorema, subst_final),
        run_time=2
    )
    s.wait(2)

    # 4. Pisahkan C_S_9 dan Z_3^3 x S_3 dengan warna
    grup_kiri = MathTex(r"C_{S_9}(\sigma)", color=BLUE_E, font_size=40).move_to(LEFT * 3.5 + UP * 0.8)
    grup_kanan = MathTex(r"\mathbb{Z}_3^3 \rtimes S_3", color=RED_E, font_size=40).move_to(RIGHT * 3.5 + UP * 0.8)

    s.play(
        FadeOut(teorema), 
        FadeIn(grup_kiri, shift=LEFT),
        FadeIn(grup_kanan, shift=RIGHT),
        run_time=1.5
    )

    # Panah melengkung
    panah_atas = CurvedArrow(grup_kiri.get_right() + RIGHT*0.2 + UP*0.2, grup_kanan.get_left() + LEFT*0.2 + UP*0.2, angle=-TAU/12, color=GRAY)
    panah_bawah = CurvedArrow(grup_kanan.get_left() + LEFT*0.2 + DOWN*0.2, grup_kiri.get_right() + RIGHT*0.2 + DOWN*0.2, angle=-TAU/12, color=GRAY)

    label_phi = MathTex(r"\Phi", color=BLACK, font_size=32).next_to(panah_atas, UP, buff=0.1)
    label_phi_inv = MathTex(r"\Phi^{-1}", color=BLACK, font_size=32).next_to(panah_bawah, DOWN, buff=0.1)

    s.play(Create(panah_atas), Write(label_phi), Create(panah_bawah), Write(label_phi_inv))
    s.wait(1)

    # 5. Animasi Pemetaan Elemen (Total 7 Elemen) dijejerin ke bawah
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
        (r"\vdots", r"\vdots"),
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
        
        s.play(
            FadeOut(panah_tengah),
            Transform(center_kiri, target_kiri),
            Transform(center_kanan, target_kanan),
            run_time=0.8
        )
        kiri_group.add(center_kiri)
        kanan_group.add(center_kanan)
        s.wait(0.3)
    

    # 6. Kotakin kedua himpunan
    kotak_kiri = SurroundingRectangle(VGroup(grup_kiri, kiri_group), color=BLUE_E, buff=0.3)
    kotak_kanan = SurroundingRectangle(VGroup(grup_kanan, kanan_group), color=RED_E, buff=0.3)

    s.play(Create(kotak_kiri), Create(kotak_kanan), run_time=1.5)
    s.wait(3)

    # Fade Out Semua
    s.play(FadeOut(VGroup(judul, sigma_tex, grup_kiri, grup_kanan, panah_atas, panah_bawah, label_phi, label_phi_inv, kiri_group, kanan_group, kotak_kiri, kotak_kanan)))