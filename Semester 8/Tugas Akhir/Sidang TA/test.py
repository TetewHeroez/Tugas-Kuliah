from manim import *
from lib.slide_tracker import *

config.background_color = WHITE

class RevisionScene(Scene):
    def construct(self):
        centralizer(self)

def centralizer(s):
    # 1. Judul & Definisi 
    judul = Title("Centralizer", color=BLACK, font_size=48, include_underline=True)
    judul[-1].set_color(BLACK)
    
    teks_atas = Tex(
    r"\parbox{"
    + str(config.frame_width)
    + r"cm}{\textbf{Definisi 3}. Centralizer dari suatu permutasi $\sigma \in S_n$ didefinisikan sebagai himpunan semua permutasi $\tau \in S_n$ yang komutatif dengan $\sigma$. Secara ekuivalen, centralizer memuat seluruh permutasi yang mempertahankan struktur sikel dari $\sigma$.}",
    color=BLACK,
    font_size=30).next_to(judul, DOWN, buff=0.5)

    definisi = MathTex(
    r"C_{S_n}(\sigma)=\{\tau\in S_n\mid\tau\sigma=\sigma\tau\}",
    color=BLACK,
    font_size=30).next_to(teks_atas, DOWN, buff=0.5)

    teks_bawah = Tex(
    r"\parbox{"
    + str(config.frame_width)
    + r"cm}{Misalkan $\sigma\in S_n$ memiliki $a_k$ sikel berpanjang $k$ untuk setiap $k=1,2,\ldots,n$. Maka}",
    color=BLACK,
    font_size=30
).next_to(definisi, DOWN, buff=0.6)

    teorema = MathTex(
        r"C_{S_n}(\sigma) \cong \prod_{k=1}^{n} \left( \mathbb{Z}_k^{a_k} \rtimes S_{a_k} \right)",
        color=BLACK, font_size=30
    ).next_to(teks_bawah, DOWN, buff=0.8)

    s.play(Write(judul), run_time=1)
    s.play(Write(teks_atas,definisi), run_time=1.5)
    s.play(Write(teks_bawah,teorema), run_time=1)
    s.wait(2)

    # 2. Transisi ke Contoh (Morphing, tanpa langkah-langkah kaku)
    teks_contoh = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{Tinjau permutasi $\sigma \in S_9$ berikut:}", color=BLACK, font_size=30).move_to(teks_atas)

    sigma_tex = MathTex(
        r"\sigma =", r"(1\;2\;3)", r"(4\;5\;6)", r"(7\;8)", r"(9)",
        color=BLACK, font_size=30
    ).next_to(teks_contoh, DOWN, buff=0.5)
    
    sigma_tex[1].set_color(BLUE_E)     # (1 2 3)
    sigma_tex[2].set_color(RED_E)      # (4 5 6)
    sigma_tex[3].set_color(GREEN_E)    # (7 8)
    sigma_tex[4].set_color(ORANGE)     # (9)

    s.play(
        Transform(teks_atas, teks_contoh),
        teorema.animate.next_to(sigma_tex, DOWN, buff=0.8),
        run_time=1.5
    )
    s.play(Write(sigma_tex), run_time=1)
    s.wait(1)

    # 3. Substitusi Teorema Langsung (Visual Morphing)
    subst_final = MathTex(
        r"C_{S_9}(\sigma) \cong (\mathbb{Z}_3^2 \rtimes S_2) \times \mathbb{Z}_2",
        color=BLACK, font_size=30
    ).move_to(teorema)

    s.play(Transform(teorema, subst_final), run_time=1.5)
    s.wait(2)

    # Bersihkan teks atas untuk fokus ke analisis
    s.play(
        FadeOut(teks_atas),
        sigma_tex.animate.next_to(judul, DOWN, buff=0.3),
        teorema.animate.next_to(judul, DOWN, buff=1.3),
        run_time=1.5
    )

    # 4. Peta Isomorfisma
    teks_peta = Tex(r"\textbf{Peta Isomorfisma ($\Phi$)}", color=BLACK, font_size=32).next_to(teorema, DOWN, buff=0.6)
    
    phi_math = MathTex(
        r"\Phi: C_{S_9}(\sigma) \longrightarrow (\mathbb{Z}_3^2 \rtimes S_2) \times \mathbb{Z}_2",
        color=BLACK, font_size=36
    ).next_to(teks_peta, DOWN, buff=0.3)
    
    phi_def = MathTex(
        r"\Phi(\tau) = ((a,b), \pi_\tau, \varepsilon)",
        color=BLACK, font_size=36
    ).next_to(phi_math, DOWN, buff=0.3)

    s.play(Write(teks_peta))
    s.play(Write(phi_math))
    s.play(Write(phi_def))
    s.wait(2)

    # Pindahkan phi_def ke atas (menyederhanakan layar)
    s.play(
        FadeOut(teks_peta), FadeOut(phi_math),
        phi_def.animate.next_to(teorema, DOWN, buff=0.5)
    )

    # --- 5. Analisis per Siklus ---
    analisa_teks = Tex(r"\textbf{Analisis per Siklus}", color=BLACK, font_size=32).next_to(phi_def, DOWN, buff=0.5)
    s.play(Write(analisa_teks))

    # Parameter a,b (3-cycle rotasi)
    s.play(
        sigma_tex[3].animate.set_color(GRAY).set_opacity(0.3),
        sigma_tex[4].animate.set_color(GRAY).set_opacity(0.3),
        run_time=1
    )

    ket_ab = Tex(r"\parbox{" + str(config.frame_width-1) + r"cm}{\textbf{$a, b \in \mathbb{Z}_3$}\\ Mewakili jumlah rotasi pada dua siklus 3. \\ Contoh: rotasi pada siklus pertama ($(1\;2\;3)^2 = (1\;3\;2)$) memiliki nilai $a=2$.}", color=BLACK, font_size=28).next_to(analisa_teks, DOWN, buff=0.4)
    s.play(Write(ket_ab))

    c1_copy = sigma_tex[1].copy()
    c2_copy = sigma_tex[2].copy()
    anim_z3 = VGroup(c1_copy, c2_copy).arrange(RIGHT, buff=0.5).next_to(ket_ab, DOWN, buff=0.5)
    s.play(TransformFromCopy(sigma_tex[1], c1_copy), TransformFromCopy(sigma_tex[2], c2_copy))
    
    p1, p2, p3 = c1_copy[1].get_center(), c1_copy[2].get_center(), c1_copy[3].get_center()
    s.play(
        c1_copy[1].animate.move_to(p2),
        c1_copy[2].animate.move_to(p3),
        c1_copy[3].animate.move_to(p1),
        path_arc=PI/2, run_time=1.5
    )
    s.wait(2)

    # Parameter \pi_\tau (3-cycle swap)
    ket_pi = Tex(r"\parbox{" + str(config.frame_width-1) + r"cm}{\textbf{$\pi_\tau \in S_2$}\\ Menentukan apakah kedua siklus 3 ditukar posisinya secara utuh.}", color=BLACK, font_size=28).move_to(ket_ab)
    
    s.play(FadeOut(ket_ab), FadeIn(ket_pi))
    
    box_b = SurroundingRectangle(c1_copy, color=BLUE_E, buff=0.1)
    box_r = SurroundingRectangle(c2_copy, color=RED_E, buff=0.1)
    s.play(Create(box_b), Create(box_r))
    g_b = VGroup(c1_copy, box_b)
    g_r = VGroup(c2_copy, box_r)
    pos_b, pos_r = g_b.get_center(), g_r.get_center()
    
    s.play(
        g_b.animate.move_to(pos_r),
        g_r.animate.move_to(pos_b),
        path_arc=PI/3, run_time=1.5
    )
    s.play(FadeOut(box_b), FadeOut(box_r))
    s.wait(2)

    # Parameter \varepsilon (2-cycle)
    s.play(FadeOut(ket_pi), FadeOut(c1_copy), FadeOut(c2_copy))

    s.play(
        sigma_tex[1].animate.set_color(GRAY).set_opacity(0.3),
        sigma_tex[2].animate.set_color(GRAY).set_opacity(0.3),
        sigma_tex[3].animate.set_color(GREEN_E).set_opacity(1),
        run_time=1
    )

    ket_eps = Tex(r"\parbox{" + str(config.frame_width-1) + r"cm}{\textbf{$\varepsilon \in \mathbb{Z}_2$}\\ Menentukan rotasi pada siklus $(7\;8)$. \\ Nilainya berupa identitas ($e$) atau berotasi menjadi $(8\;7)$.}", color=BLACK, font_size=28).move_to(ket_ab)
    s.play(Write(ket_eps))

    c3_copy = sigma_tex[3].copy().next_to(ket_eps, DOWN, buff=0.5)
    s.play(TransformFromCopy(sigma_tex[3], c3_copy))

    p7, p8 = c3_copy[1].get_center(), c3_copy[2].get_center()
    s.play(
        c3_copy[1].animate.move_to(p8),
        c3_copy[2].animate.move_to(p7),
        path_arc=PI/2, run_time=1.5
    )
    s.wait(2)

    s.play(FadeOut(ket_eps), FadeOut(c3_copy), FadeOut(analisa_teks))

    # Reset opacity
    s.play(
        sigma_tex[1].animate.set_color(BLUE_E).set_opacity(1),
        sigma_tex[2].animate.set_color(RED_E).set_opacity(1),
        sigma_tex[3].animate.set_color(GREEN_E).set_opacity(1),
        sigma_tex[4].animate.set_color(ORANGE).set_opacity(1),
        run_time=1
    )
    
    # 6. Kesimpulan elemen
    judul_elemen = Tex(r"\textbf{Kesimpulan}", color=BLACK, font_size=32).next_to(phi_def, DOWN, buff=0.5)
    s.play(Write(judul_elemen))

    kesimpulan = Tex(r"\parbox{" + str(config.frame_width-1) + r"cm}{Ketiga parameter $(a,b), \pi_\tau, \varepsilon$ divariasikan secara bebas untuk membentuk seluruh elemen di $C_{S_9}(\sigma)$.\\ \vspace{0.2cm} $|C_{S_9}(\sigma)| = (3^2 \cdot 2!) \cdot 2 = 36$ elemen.}", color=BLACK, font_size=30).next_to(judul_elemen, DOWN, buff=0.4)
    
    s.play(Write(kesimpulan))
    s.wait(4)

    s.play(FadeOut(VGroup(judul, teorema, sigma_tex, phi_def, judul_elemen, kesimpulan)))