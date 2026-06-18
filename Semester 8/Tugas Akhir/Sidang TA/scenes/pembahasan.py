from manim import *

from lib.slide_tracker import *


def pembahasan(s):
    kriteria_komutativitas(s)
    next_slide_count(s)
    algoritma_pencarian(s)
    next_slide_count(s)
    hasil_penerapan(s)


def make_text_box(title, body, color, width=4.2, font_size=25):
    title_tex = Tex(title, color=BLACK, font_size=30)
    body_tex = Tex(
        r"\parbox{" + str(width) + r"cm}{" + body + r"}",
        color=BLACK,
        font_size=font_size,
    )
    body_tex.next_to(title_tex, DOWN, buff=0.2)
    frame = RoundedRectangle(
        corner_radius=0.2,
        width=max(title_tex.width, body_tex.width) + 0.6,
        height=title_tex.height + body_tex.height + 0.8,
        stroke_color=color,
        fill_color=color,
        fill_opacity=0.18,
        stroke_width=2,
    )
    content = VGroup(title_tex, body_tex)
    content.move_to(frame.get_center())
    return VGroup(frame, content)


def kriteria_komutativitas(s):
    title = Title("Pembahasan", color=BLACK, font_size=48, include_underline=True)
    title[-1].set_color(BLACK)

    persamaan = MathTex(r"A \otimes B = B \otimes A", color=DARK_BROWN, font_size=42)
    persamaan.next_to(title, DOWN, buff=0.5)

    card_perlu = make_text_box(
        r"\textbf{Syarat perlu}",
        r"Jika $A$ dan $B$ komutatif, maka $\sigma_n^B \in C_{S_n}(\sigma_n^A)$.",
        BLUE_E,
    )
    card_cukup = make_text_box(
        r"\textbf{Syarat cukup}",
        r"Komutativitas dijamin bila seluruh permutasi penyusun berada pada subgrup abelian yang sama.",
        GREEN_E,
    )
    card_superlevel = make_text_box(
        r"\textbf{Kriteria perlu-cukup}",
        r"$\mathcal{U}_{\ge v}^{AB}=\mathcal{U}_{\ge v}^{BA}$ untuk setiap level $v=n+2,\ldots,2n$.",
        ORANGE,
    )
    cards = VGroup(card_perlu, card_cukup, card_superlevel).arrange(RIGHT, buff=0.45)
    cards.scale(0.9)
    cards.next_to(persamaan, DOWN, buff=0.7)

    arrows = VGroup()
    for card in cards:
        arrow = Arrow(
            start=persamaan.get_bottom(),
            end=card.get_top(),
            buff=0.15,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.18,
            color=GRAY_B,
        )
        arrows.add(arrow)

    summary = Tex(
        r"\parbox{12cm}{Kriteria pada Bab 4 dipakai untuk menyaring kandidat $B$ sejak level tertinggi, lalu diverifikasi bertahap sampai membentuk \textit{Latin square} lengkap.}",
        color=BLACK,
        font_size=28,
    ).to_edge(DOWN, buff=0.5)

    s.play(Write(title), Write(persamaan), run_time=1)
    for card, arrow in zip(cards, arrows):
        s.play(GrowArrow(arrow), FadeIn(card, shift=UP * 0.2), run_time=0.8)
    s.play(Write(summary), run_time=0.8)
    s.wait(1)
    s.next_slide()
    s.play(FadeOut(VGroup(title, persamaan, cards, arrows, summary), shift=LEFT), run_time=1)


def algoritma_pencarian(s):
    title = Title("Algoritma Pencarian", color=BLACK, font_size=48, include_underline=True)
    title[-1].set_color(BLACK)

    def process_box(text, width=3.5, height=1.1, color=YELLOW_E):
        box = RoundedRectangle(
            corner_radius=0.15,
            width=width,
            height=height,
            stroke_color=BLACK,
            fill_color=color,
            fill_opacity=0.8,
        )
        label = Text(text, color=BLACK, font_size=22, line_spacing=0.9).move_to(box)
        return VGroup(box, label)

    input_box = process_box("Input Latin square A", width=3.8, color=BLUE_B)
    dekomposisi = process_box("Dekomposisi\nA = sum i otimes P_sigma_i^A", width=3.8, height=1.25)
    decision_shape = Square(side_length=1.8, color=BLACK, fill_color=GRAY_E, fill_opacity=1).rotate(PI / 4)
    decision_text = Text("Permutasi\nA saling\nkomutatif?", color=BLACK, font_size=20, line_spacing=0.8)
    decision = VGroup(decision_shape, decision_text)

    alt_1 = process_box("Tahap alternatif:\nbentuk H_A", width=3.4, height=1.2, color=GREEN_B)
    alt_2 = process_box("Susun ulang\nperm. penyusun A", width=3.4, height=1.2, color=GREEN_C)

    gen_1 = process_box("Tahap umum:\npilih dari centralizer", width=3.6, height=1.2, color=ORANGE)
    gen_2 = process_box("Isi B* lalu cek\nsuperlevel", width=3.6, height=1.2, color=ORANGE)

    hasil = process_box("Kandidat B in P(A)", width=4.0, color=TEAL_B)

    input_box.move_to(UP * 2.8)
    dekomposisi.next_to(input_box, DOWN, buff=0.55)
    decision.next_to(dekomposisi, DOWN, buff=0.6)
    alt_1.move_to(LEFT * 3.2 + DOWN * 1.4)
    alt_2.next_to(alt_1, DOWN, buff=0.45)
    gen_1.move_to(RIGHT * 3.2 + DOWN * 1.4)
    gen_2.next_to(gen_1, DOWN, buff=0.45)
    hasil.move_to(DOWN * 3.45)

    arrows = VGroup(
        Arrow(input_box.get_bottom(), dekomposisi.get_top(), buff=0.1, color=BLACK),
        Arrow(dekomposisi.get_bottom(), decision.get_top(), buff=0.1, color=BLACK),
        Arrow(decision.get_bottom() + LEFT * 0.6, alt_1.get_top(), buff=0.1, color=BLACK),
        Arrow(alt_1.get_bottom(), alt_2.get_top(), buff=0.1, color=BLACK),
        Arrow(decision.get_bottom() + RIGHT * 0.6, gen_1.get_top(), buff=0.1, color=BLACK),
        Arrow(gen_1.get_bottom(), gen_2.get_top(), buff=0.1, color=BLACK),
        Arrow(alt_2.get_bottom(), hasil.get_top() + LEFT * 0.9, buff=0.1, color=BLACK),
        Arrow(gen_2.get_bottom(), hasil.get_top() + RIGHT * 0.9, buff=0.1, color=BLACK),
    )

    yes_label = Text("Ya", color=GREEN_E, font_size=22).next_to(arrows[2], LEFT, buff=0.1)
    no_label = Text("Tidak", color=RED_E, font_size=22).next_to(arrows[4], RIGHT, buff=0.1)

    note = Tex(
        r"\parbox{12.5cm}{Tahap alternatif memanfaatkan subgrup abelian. Jika kondisi itu gagal, algoritma berpindah ke tahap umum melalui \emph{centralizer} simbol maksimum dan pemeriksaan himpunan superlevel secara menurun.}",
        color=BLACK,
        font_size=27,
    ).to_edge(DOWN, buff=0.25)

    s.play(Write(title), run_time=0.8)
    s.play(FadeIn(input_box), GrowArrow(arrows[0]), FadeIn(dekomposisi), run_time=1)
    s.play(GrowArrow(arrows[1]), FadeIn(decision), run_time=0.8)
    s.play(
        GrowArrow(arrows[2]),
        Write(yes_label),
        FadeIn(alt_1, shift=LEFT * 0.2),
        GrowArrow(arrows[3]),
        FadeIn(alt_2, shift=LEFT * 0.2),
        run_time=1,
    )
    s.play(Circumscribe(VGroup(alt_1, alt_2), color=GREEN_E), run_time=0.8)
    s.play(
        GrowArrow(arrows[4]),
        Write(no_label),
        FadeIn(gen_1, shift=RIGHT * 0.2),
        GrowArrow(arrows[5]),
        FadeIn(gen_2, shift=RIGHT * 0.2),
        run_time=1,
    )
    s.play(Circumscribe(VGroup(gen_1, gen_2), color=ORANGE), run_time=0.8)
    s.play(
        GrowArrow(arrows[6]),
        GrowArrow(arrows[7]),
        FadeIn(hasil, shift=UP * 0.2),
        Write(note),
        run_time=1,
    )
    s.wait(1)
    s.next_slide()
    s.play(
        FadeOut(
            VGroup(
                title,
                input_box,
                dekomposisi,
                decision,
                alt_1,
                alt_2,
                gen_1,
                gen_2,
                hasil,
                arrows,
                yes_label,
                no_label,
                note,
            ),
            shift=LEFT,
        ),
        run_time=1,
    )


def hasil_penerapan(s):
    title = Title("Penerapan Pada Ordo 3, 4, dan 5", color=BLACK, font_size=44, include_underline=True)
    title[-1].set_color(BLACK)

    card_3 = make_text_box(
        r"\textbf{Ordo 3}",
        r"$C_{S_3}((1\;3))=\{(1),(1\;3)\}$ sehingga kandidat awal untuk simbol maksimum langsung menyempit.",
        BLUE_D,
        width=3.7,
        font_size=23,
    )
    card_4 = make_text_box(
        r"\textbf{Ordo 4}",
        r"Muncul dua pola: tahap alternatif saat permutasi membentuk grup Klein, dan tahap umum saat perlu \emph{centralizer} serta superlevel.",
        GREEN_D,
        width=3.9,
        font_size=23,
    )
    card_5 = make_text_box(
        r"\textbf{Ordo 5}",
        r"Kasus siklik memakai tahap alternatif, sedangkan contoh non-abelian tetap dapat ditangani lewat penyaringan bertahap.",
        ORANGE,
        width=3.8,
        font_size=23,
    )
    cards = VGroup(card_3, card_4, card_5).arrange(RIGHT, buff=0.4)
    cards.scale(0.92)
    cards.next_to(title, DOWN, buff=0.7)

    badges = VGroup(
        Text("Tahap umum", color=WHITE, font_size=20, weight=BOLD),
        Text("Alternatif + umum", color=WHITE, font_size=20, weight=BOLD),
        Text("Alternatif + umum", color=WHITE, font_size=20, weight=BOLD),
    )
    badge_boxes = VGroup()
    for badge, card, color in zip(badges, cards, [BLUE_E, GREEN_E, ORANGE]):
        pill = RoundedRectangle(
            corner_radius=0.2,
            width=badge.width + 0.45,
            height=0.5,
            stroke_width=0,
            fill_color=color,
            fill_opacity=1,
        )
        badge.move_to(pill)
        badge_group = VGroup(pill, badge).next_to(card, UP, buff=0.18)
        badge_boxes.add(badge_group)

    takeaway = Tex(
        r"\parbox{11.5cm}{Dari seluruh contoh pada Bab 4, pola yang konsisten adalah: \emph{centralizer} memberi penyaringan awal untuk simbol maksimum, sedangkan himpunan superlevel memastikan kandidat yang tersisa benar-benar komutatif.}",
        color=BLACK,
        font_size=28,
    ).to_edge(DOWN, buff=0.45)

    s.play(Write(title), run_time=0.8)
    for badge, card in zip(badge_boxes, cards):
        s.play(FadeIn(badge, shift=UP * 0.1), FadeIn(card, shift=UP * 0.2), run_time=0.8)
    s.play(Write(takeaway), run_time=0.8)
    s.wait(1)
    s.next_slide(auto_next=True)
    s.play(FadeOut(VGroup(title, cards, badge_boxes, takeaway), scale=0.5), run_time=1)
