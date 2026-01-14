from manim import *

class WelcomeToManim(Scene):
    def construct(self):
        number = ValueTracker(1)
        words = Text(f"{number.get_value()}")
        banner = ManimBanner().scale(0.5)
        VGroup(words, banner).arrange(DOWN)

        turn_animation_into_updater(Write(words, run_time=0.9))
        self.add(words)
        for i in range(2, 11):
            number.animate.set_value(i)
        self.wait(0.5)
        self.play(banner.expand(), run_time=0.5)
        
class AlignedComparison(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{amssymb}")

        # UKURAN KOLOM
        width_col = (config.frame_width / 2) - 0.5
        
        # --- KONTEN KIRI (STICKEL) ---
        l_intro = Tex(
            r"\parbox{" + str(width_col) + r"cm}{"
            r"Misalkan $G$ adalah grup non-abelian hingga, dan $a, b \in G$ dengan $ab \neq ba$."
            r"}", font_size=24, color=BLACK
        )
        l_item1 = Tex(
            r"\parbox{" + str(width_col) + r"cm}{"
            r"$\bullet$ Bob memilih $r, s \in \mathbb{N}$, kemudian mengirimkan $c = a^r b^s$ kepada Alice."
            r"}", font_size=24, color=BLACK
        )
        l_item2 = Tex(
            r"\parbox{" + str(width_col) + r"cm}{"
            r"$\bullet$ Alice memilih $v, w \in \mathbb{N}$, kemudian mengirimkan $d = a^v b^w$ kepada Bob."
            r"}", font_size=24, color=BLACK
        )
        l_item3 = Tex(
            r"\parbox{" + str(width_col) + r"cm}{"
            r"$\bullet$ Alice menghitung kunci bersama $k = a^v c b^w$."
            r"}", font_size=24, color=BLACK
        )
        l_item4 = Tex(
            r"\parbox{" + str(width_col) + r"cm}{"
            r"$\bullet$ Bob dengan cara yang sama menghitung $k = a^r d b^s$."
            r"}", font_size=24, color=BLACK
        )

        left_group = VGroup(l_intro, l_item1, l_item2, l_item3, l_item4)
        left_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        left_group.to_edge(LEFT, buff=0.2)


        # --- KONTEN KANAN (TROPIKAL) ---
        r_intro = Tex(
            r"\parbox{" + str(width_col) + r"cm}{"
            r"Misalkan matriks $W \in \mathbb{R}_{\max}^{n \times n}$ disepakati sebagai matriks publik."
            r"}", font_size=24, color=BLACK
        )
        r_item1 = Tex(
            r"\parbox{" + str(width_col) + r"cm}{"
            r"$\bullet$ Alice memilih matriks acak $A_1, A_2$, kemudian mengirimkan $U = A_1 \otimes W \otimes A_2$ kepada Bob."
            r"}", font_size=24, color=BLACK
        )
        r_item2 = Tex(
            r"\parbox{" + str(width_col) + r"cm}{"
            r"$\bullet$ Bob memilih matriks acak $B_1, B_2$, kemudian mengirimkan $V = B_1 \otimes W \otimes B_2$ kepada Alice."
            r"}", font_size=24, color=BLACK
        )
        r_item3 = Tex(
            r"\parbox{" + str(width_col) + r"cm}{"
            r"$\bullet$ Alice menghitung kunci bersama $K = A_1 \otimes V \otimes A_2$."
            r"}", font_size=24, color=BLACK
        )
        r_item4 = Tex(
            r"\parbox{" + str(width_col) + r"cm}{"
            r"$\bullet$ Bob dengan cara yang sama menghitung $K = B_1 \otimes U \otimes B_2$."
            r"}", font_size=24, color=BLACK
        )

        right_group = VGroup(r_intro, r_item1, r_item2, r_item3, r_item4)
        
        # LOGIKA ALIGNMENT: 
        # Paksa setiap item Kanan sejajar ATAS (UP) dengan item Kiri pasangannya
        r_intro.next_to(l_intro, RIGHT, buff=0.5, aligned_edge=UP)
        r_item1.next_to(l_item1, RIGHT, buff=0.5, aligned_edge=UP)
        r_item2.next_to(l_item2, RIGHT, buff=0.5, aligned_edge=UP)
        r_item3.next_to(l_item3, RIGHT, buff=0.5, aligned_edge=UP)
        r_item4.next_to(l_item4, RIGHT, buff=0.5, aligned_edge=UP)
        
        # GARIS PEMBATAS
        separator = Line(UP*3.5, DOWN*3.5, color=GRAY)
        
        # HEADER KIRI (Sudah kamu buat sebelumnya)
        header_left = Title("Protokol Stickel", color=BLACK, font_size=30, match_underline_width_to_text=True)
        header_left[1].set_color(BLACK)
        header_left.move_to(left_group.get_top() + UP*1).shift(RIGHT*1) # Sesuaikan manual

        # Animasi
        self.play(Write(header_left))
        self.play(
            LaggedStart(
                Write(left_group),
                Create(separator),
                Write(right_group),
                lag_ratio=0.1
            ),
            run_time=4
        )
        self.wait()

class TwoColumnLayout(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{enumitem}")

        isi_latex = r"""
        Misalkan $G$ adalah grup non-abelian hingga, dan $a, b \in G$ dengan $ab \neq ba$.
        \begin{itemize}[label=$\bullet$, leftmargin=0.5cm]
            \item Bob memilih $r, s \in \mathbb{N}$, kemudian mengirimkan $c = a^{r} b^{s}$ kepada Alice.
            \item Alice memilih $v, w \in \mathbb{N}$, kemudian mengirimkan $d = a^{v} b^{w}$ kepada Bob.
            \item Alice menghitung kunci bersama $k= a^v c b^w$.
            \item Bob dengan cara yang sama menghitung $k = a^r d b^s$. 
        \end{itemize}
        """

        lebar_penuh = f"{config.frame_width - 2}cm"
        algoritma_full = Tex(
            r"\parbox{" + lebar_penuh + r"}{" + isi_latex + r"}", 
            font_size=30,
            color=BLACK,
            tex_template=my_template
        )
        algoritma_full.to_edge(LEFT, buff=1)

        lebar_setengah = f"{config.frame_width / 2 }cm"
        algoritma_col = Tex(
            r"\parbox{" + lebar_setengah + r"}{" + isi_latex + r"}", 
            font_size=30, 
            color=BLACK,
            tex_template=my_template
        )
        algoritma_col.to_edge(LEFT, buff=0.5)

        self.add(algoritma_full)
        self.wait()

        self.play(
            ReplacementTransform(algoritma_full, algoritma_col),
            run_time=2
        )
        
        garis_tengah = DashedLine(UP*3, DOWN*3, color=GRAY).next_to(algoritma_col, RIGHT, buff=0.5)
        konten_baru = Text("Konten Kolom Kanan", color=BLUE, font_size=24).next_to(garis_tengah, RIGHT)
        
        self.play(Create(garis_tengah), Write(konten_baru))
        self.wait()