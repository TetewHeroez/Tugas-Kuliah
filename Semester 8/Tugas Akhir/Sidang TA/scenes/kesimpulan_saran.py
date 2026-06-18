from manim import *

from lib.slide_tracker import *


def kesimpulan_saran(s):
    kesimpulan_utama(s)
    next_slide_count(s)
    saran_penelitian(s)


def make_summary_card(label, body, color):
    tag_text = Text(label, color=WHITE, font_size=22, weight=BOLD)
    tag = RoundedRectangle(
        corner_radius=0.18,
        width=tag_text.width + 0.6,
        height=0.7,
        stroke_width=0,
        fill_color=color,
        fill_opacity=1,
    )
    tag_text.move_to(tag)

    body_tex = Tex(
        r"\parbox{4.9cm}{" + body + r"}",
        color=BLACK,
        font_size=27,
    )
    box = RoundedRectangle(
        corner_radius=0.2,
        width=body_tex.width + 0.8,
        height=body_tex.height + 1.2,
        stroke_color=color,
        fill_color=color,
        fill_opacity=0.16,
        stroke_width=2,
    )
    body_tex.move_to(box.get_center()).shift(DOWN * 0.15)
    badge = VGroup(tag, tag_text).next_to(box, UP, buff=-0.15)
    return VGroup(box, badge, body_tex)


def kesimpulan_utama(s):
    title = Title("Kesimpulan", color=BLACK, font_size=48, include_underline=True)
    title[-1].set_color(BLACK)

    intro = Tex(
        r"\parbox{12.5cm}{Bab 5 merangkum tiga hasil utama penelitian: syarat perlu, kriteria komutativitas, dan konstruksi pasangan \textit{Latin square} komutatif.}",
        color=BLACK,
        font_size=30,
    ).next_to(title, DOWN, buff=0.45)

    card_1 = make_summary_card(
        "Syarat perlu",
        r"Jika $A$ dan $B$ komutatif, maka permutasi simbol maksimum pada $B$ harus berada pada \emph{centralizer} dari permutasi simbol maksimum pada $A$.",
        BLUE_E,
    )
    card_2 = make_summary_card(
        "Kriteria",
        r"Komutativitas dijamin oleh subgrup abelian yang sama, dan juga dapat diuji lewat kesamaan himpunan superlevel pada setiap level penting.",
        GREEN_E,
    )
    card_3 = make_summary_card(
        "Konstruksi",
        r"Algoritma pencarian menyatukan tahap alternatif dan tahap umum sehingga kandidat $B$ dapat dibangun secara sistematis.",
        ORANGE,
    )
    cards = VGroup(card_1, card_2, card_3).arrange(RIGHT, buff=0.35)
    cards.scale(0.9)
    cards.next_to(intro, DOWN, buff=0.65)

    footer = MathTex(r"A \otimes B = B \otimes A", color=DARK_BROWN, font_size=40)
    footer.next_to(cards, DOWN, buff=0.55)

    s.play(Write(title), Write(intro), run_time=1)
    for card in cards:
        s.play(FadeIn(card, shift=UP * 0.2), run_time=0.75)
    s.play(Write(footer), run_time=0.6)
    s.wait(1)
    s.next_slide()
    s.play(FadeOut(VGroup(title, intro, cards, footer), shift=LEFT), run_time=1)


def saran_penelitian(s):
    title = Title("Saran", color=BLACK, font_size=48, include_underline=True)
    title[-1].set_color(BLACK)

    roadmap_line = Line(LEFT * 5.5, RIGHT * 5.5, color=GRAY_B, stroke_width=3)
    roadmap_line.next_to(title, DOWN, buff=1.1)

    suggestions = [
        ("Implementasi", r"Mengimplementasikan algoritma secara komputasi untuk ordo yang lebih besar.", BLUE_E),
        ("Efisiensi", r"Mengkaji pemeriksaan superlevel agar proses pencarian kandidat menjadi lebih cepat.", GREEN_E),
        ("Generalisasi", r"Mengembangkan syarat cukup melalui subgrup abelian ke bentuk yang lebih umum berbasis \emph{centralizer}.", ORANGE),
    ]

    nodes = VGroup()
    cards = VGroup()
    for i, (label, body, color) in enumerate(suggestions):
        node = Dot(color=color, radius=0.12)
        node.move_to(roadmap_line.point_from_proportion((i + 1) / 4))
        nodes.add(node)

        card = make_summary_card(label, body, color)
        if i % 2 == 0:
            card.next_to(node, UP, buff=0.45)
        else:
            card.next_to(node, DOWN, buff=0.45)
        cards.add(card)

    connectors = VGroup()
    for node, card in zip(nodes, cards):
        target = card[0].get_bottom() if card.get_center()[1] > node.get_center()[1] else card[0].get_top()
        connectors.add(Line(node.get_center(), target, color=GRAY_C, stroke_width=2))

    closing = Tex(
        r"\parbox{12cm}{Ketiga saran tersebut membuka peluang lanjutan: dari validasi komputasi, optimasi algoritma, hingga penguatan hasil teoritis pada struktur permutasi yang lebih umum.}",
        color=BLACK,
        font_size=28,
    ).to_edge(DOWN, buff=0.35)

    s.play(Write(title), Create(roadmap_line), run_time=0.8)
    for node, connector, card in zip(nodes, connectors, cards):
        s.play(FadeIn(node), Create(connector), FadeIn(card, shift=UP * 0.1), run_time=0.8)
    s.play(Write(closing), run_time=0.7)
    s.wait(1)
    s.next_slide(auto_next=True)
    s.play(FadeOut(VGroup(title, roadmap_line, nodes, connectors, cards, closing), scale=0.5), run_time=1)
