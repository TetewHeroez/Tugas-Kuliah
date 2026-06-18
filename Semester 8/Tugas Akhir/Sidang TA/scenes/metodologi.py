from manim import *

from lib.slide_tracker import *


def metodologi(s):
    flowchart(s)


def flowchart(s):
    my_template = TexTemplate()
    my_template.add_to_preamble(r"\usepackage{xcolor}")

    C_START = "#FFB6C1"
    C_PROC = "#FFFACD"
    C_STROKE = BLACK
    TXT_COLOR = BLACK
    DOT_COLOR = RED
    CIRCUM_COLOR = ORANGE

    steps_data = [
        ("Mulai", C_START),
        ("Studi Literatur", C_PROC),
        ("Identifikasi Latin\nsquare Komutatif", C_PROC),
        ("Investigasi Sifat\nLatin square Komutatif", C_PROC),
        ("Penyusunan Algoritma\nLatin square Komutatif", C_PROC),
        ("Penarikan\nKesimpulan", C_PROC),
        ("Penulisan\nTugas Akhir", C_PROC),
        ("Selesai", C_START),
    ]
    desc_texts = [
        "",
        r"\color{black}Mempelajari literatur yang berkaitan dengan aljabar \textit{max-plus}, permutasi, \textit{centralizer}, dan \textit{Latin square}.",
        r"\color{black}Mengidentifikasi \textit{Latin square} seperti apa yang dapat komutatif terhadap perkalian \textit{max-plus}.",
        r"\color{black}Menganalisis struktur pasangan komutatif melalui elemen maksimum, subgrup abelian, dan himpunan superlevel.",
        r"\color{black}Menyusun algoritma pencarian pasangan komutatif dengan tahap alternatif dan tahap umum berbasis \textit{centralizer}.",
        r"\color{black}Merangkum hasil investigasi untuk menjawab rumusan masalah dan memperoleh kriteria komutativitas.",
        r"\color{black}Menyusun laporan tugas akhir berdasarkan seluruh hasil penelitian.",
        "",
    ]

    node_positions = [
        LEFT * 6.3 + UP * 1.8,
        LEFT * 3.7 + UP * 1.8,
        LEFT * 1.0 + UP * 1.8,
        RIGHT * 1.8 + UP * 1.8,
        RIGHT * 1.8 + DOWN * 1.0,
        LEFT * 1.0 + DOWN * 1.0,
        LEFT * 3.7 + DOWN * 1.0,
        LEFT * 6.3 + DOWN * 1.0,
    ]

    nodes = VGroup()
    for i, ((title, color), position) in enumerate(zip(steps_data, node_positions)):
        if i == 0 or i == len(steps_data) - 1:
            box = Circle(
                radius=0.95,
                fill_color=color,
                fill_opacity=1,
                stroke_color=C_STROKE,
                stroke_width=2,
            )
        else:
            box = Rectangle(
                width=3.6,
                height=1.45,
                fill_color=color,
                fill_opacity=1,
                stroke_color=C_STROKE,
                stroke_width=2,
            )
        box.move_to(position)
        text = Text(title, font_size=20, color=TXT_COLOR, line_spacing=0.95).move_to(box.get_center())
        nodes.add(VGroup(box, text))

    arrows = VGroup(
        Arrow(nodes[0].get_right(), nodes[1].get_left(), color=BLACK, buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.15),
        Arrow(nodes[1].get_right(), nodes[2].get_left(), color=BLACK, buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.15),
        Arrow(nodes[2].get_right(), nodes[3].get_left(), color=BLACK, buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.15),
        Arrow(nodes[3].get_bottom(), nodes[4].get_top(), color=BLACK, buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.15),
        Arrow(nodes[4].get_left(), nodes[5].get_right(), color=BLACK, buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.15),
        Arrow(nodes[5].get_left(), nodes[6].get_right(), color=BLACK, buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.15),
        Arrow(nodes[6].get_left(), nodes[7].get_right(), color=BLACK, buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.15),
    )

    full_chart = VGroup(nodes, arrows)
    full_chart.move_to(ORIGIN)

    s.camera.frame.move_to(full_chart.get_center())
    s.camera.frame.set(width=full_chart.width * 1.12)
    s.play(DrawBorderThenFill(nodes), Create(arrows), run_time=1)
    s.wait(0.5)
    s.camera.frame.save_state()

    def create_desc(index, node):
        desc_obj = Tex(
            r"\parbox{5.9cm}{\centering " + desc_texts[index] + r"}",
            font_size=24,
            color=BLACK,
            tex_template=my_template,
        )
        is_up = node.get_center()[1] >= 0
        if is_up:
            desc_obj.next_to(node, UP, buff=0.65)
        else:
            desc_obj.next_to(node, DOWN, buff=0.65)

        connector = Line(
            node.get_top() if is_up else node.get_bottom(),
            desc_obj.get_bottom() if is_up else desc_obj.get_top(),
            color=GRAY,
            stroke_width=1,
        )
        return VGroup(desc_obj, connector)

    process_indices = [1, 2, 3, 4, 5, 6]
    chunks = [[1, 2], [3, 4], [5, 6]]

    current_desc_group = VGroup()
    last_visited_idx = 0
    for chunk in chunks:
        group_mobjects = VGroup(*[nodes[i] for i in chunk])
        target_center = group_mobjects.get_center()
        target_width = max(group_mobjects.width * 1.35, 7.5)
        travel_dot = Dot(color=DOT_COLOR, radius=0.1)
        entrance_arrow = arrows[last_visited_idx]

        if len(current_desc_group) > 0:
            s.play(FadeOut(current_desc_group), run_time=0.3)
            current_desc_group = VGroup()

        s.play(
            s.camera.frame.animate.move_to(target_center).set(width=target_width),
            MoveAlongPath(travel_dot, entrance_arrow),
            run_time=1,
        )
        s.remove(travel_dot)
        s.wait(0.3)

        for local_idx, idx in enumerate(chunk):
            node = nodes[idx]
            if local_idx > 0:
                internal_dot = Dot(color=DOT_COLOR, radius=0.1)
                s.play(MoveAlongPath(internal_dot, arrows[idx - 1]), run_time=0.9)
                s.remove(internal_dot)

            desc_grp = create_desc(idx, node)
            s.play(
                Circumscribe(node[0], color=CIRCUM_COLOR, time_width=0.75, buff=0),
                Write(desc_grp),
                run_time=1,
            )
            current_desc_group.add(desc_grp)
            last_visited_idx = idx

        s.next_slide()

    if len(current_desc_group) > 0:
        s.play(FadeOut(current_desc_group), run_time=0.3)

    final_dot = Dot(color=DOT_COLOR, radius=0.1)
    s.play(
        Restore(s.camera.frame),
        MoveAlongPath(final_dot, arrows[last_visited_idx]),
        run_time=1,
    )
    s.remove(final_dot)
    s.wait(0.4)

    start_node = nodes[0]
    end_node = nodes[-1]
    middle_nodes = VGroup(*[nodes[i] for i in range(1, len(nodes) - 1)])

    next_slide_count(s)
    s.play(
        FadeOut(start_node),
        FadeOut(end_node),
        FadeOut(arrows),
        middle_nodes.animate.arrange(RIGHT, buff=0.35).to_edge(DOWN, buff=0.45).scale(0.72),
        run_time=1,
    )

    def create_cell_rect(width, height, x, y):
        rect = Rectangle(width=width, height=height, stroke_color=BLACK, stroke_width=1.5)
        rect.move_to([x + width / 2, y - height / 2, 0])
        return rect

    TABLE_ORIGIN = UP * 2.45 + LEFT * 6
    ROW_H = 0.62
    COL_NO_W = 0.8
    COL_NAME_W = 6.8
    COL_WEEK_W = 0.4
    BAR_COLOR = "#0072BD"

    header_group = VGroup()
    h_no_rect = create_cell_rect(COL_NO_W, ROW_H * 2, TABLE_ORIGIN[0], TABLE_ORIGIN[1])
    h_no_txt = Text("NO", font_size=24, color=BLACK).move_to(h_no_rect)
    header_group.add(h_no_rect, h_no_txt)

    h_name_rect = create_cell_rect(COL_NAME_W, ROW_H * 2, TABLE_ORIGIN[0] + COL_NO_W, TABLE_ORIGIN[1])
    h_name_txt = Text("NAMA KEGIATAN", font_size=24, color=BLACK).move_to(h_name_rect)
    header_group.add(h_name_rect, h_name_txt)

    total_month_w = COL_WEEK_W * 12
    h_bulan_rect = create_cell_rect(total_month_w, ROW_H, TABLE_ORIGIN[0] + COL_NO_W + COL_NAME_W, TABLE_ORIGIN[1])
    h_bulan_txt = Text("BULAN", font_size=24, color=BLACK).move_to(h_bulan_rect)
    header_group.add(h_bulan_rect, h_bulan_txt)

    curr_x = TABLE_ORIGIN[0] + COL_NO_W + COL_NAME_W
    curr_y = TABLE_ORIGIN[1] - ROW_H
    for month in range(1, 4):
        month_w = COL_WEEK_W * 4
        hm_rect = create_cell_rect(month_w, ROW_H / 2, curr_x, curr_y)
        hm_txt = Text(str(month), font_size=18, color=BLACK).move_to(hm_rect)
        header_group.add(hm_rect, hm_txt)

        week_y = curr_y - ROW_H / 2
        week_x = curr_x
        for week in range(1, 5):
            hw_rect = create_cell_rect(COL_WEEK_W, ROW_H / 2, week_x, week_y)
            hw_txt = Text(str(week), font_size=12, color=BLACK).move_to(hw_rect)
            header_group.add(hw_rect, hw_txt)
            week_x += COL_WEEK_W
        curr_x += month_w

    tabel_data = steps_data[1:-1]
    target_rows = VGroup()
    y_data_start = TABLE_ORIGIN[1] - (ROW_H * 2)
    for i, (title, _) in enumerate(tabel_data):
        row_y = y_data_start - (i * ROW_H)
        no_rect = create_cell_rect(COL_NO_W, ROW_H, TABLE_ORIGIN[0], row_y)
        no_txt = Text(str(i + 1), font_size=20, color=BLACK).move_to(no_rect)

        name_rect = create_cell_rect(COL_NAME_W, ROW_H, TABLE_ORIGIN[0] + COL_NO_W, row_y)
        clean_title = title.replace("\n", " ")
        name_txt = Text(clean_title, font_size=19, color=BLACK, t2s={"Latin square": ITALIC})
        max_text_width = COL_NAME_W - 0.4
        if name_txt.width > max_text_width:
            name_txt.scale(max_text_width / name_txt.width)
        name_txt.align_to(name_rect, LEFT).shift(RIGHT * 0.2)
        name_txt.match_y(name_rect)

        grid_group = VGroup()
        grid_x_start = TABLE_ORIGIN[0] + COL_NO_W + COL_NAME_W
        for week in range(12):
            grid_group.add(create_cell_rect(COL_WEEK_W, ROW_H, grid_x_start + (week * COL_WEEK_W), row_y))

        target_rows.add(VGroup(no_rect, no_txt, name_rect, name_txt, grid_group))

    jadwal_kegiatan = Title(
        "Jadwal Kegiatan",
        font_size=28,
        color=BLACK,
        include_underline=True,
        match_underline_width_to_text=True,
    )
    jadwal_kegiatan[1].set_color(BLACK)
    jadwal_kegiatan.move_to(header_group.get_top() + UP * 0.5)

    s.play(
        s.camera.frame.animate.move_to(header_group.get_center() + DOWN * 1.55).set(width=header_group.width * 1.28),
        FadeIn(header_group),
        Write(jadwal_kegiatan),
        run_time=0.5,
    )

    schedule_config = [
        (0, 2),
        (1, 3),
        (3, 5),
        (5, 4),
        (7, 3),
        (9, 3),
    ]

    for i in range(len(target_rows)):
        row = target_rows[i]
        s.play(Create(row[0]), Create(row[2]), Create(row[4]), run_time=0.25)

        start_idx, duration = schedule_config[i]
        bar = Rectangle(
            width=duration * COL_WEEK_W,
            height=ROW_H,
            fill_color=BAR_COLOR,
            fill_opacity=1,
            stroke_color=BLACK,
            stroke_width=1,
        )
        target_cell = row[4][start_idx]
        bar.align_to(target_cell, LEFT)
        bar.match_y(target_cell)

        node_box = middle_nodes[i][0]
        node_text = middle_nodes[i][1]
        s.play(
            Transform(node_box, bar),
            Transform(node_text, row[3]),
            Write(row[1]),
            lag_ratio=0.25,
            run_time=0.45,
        )

    s.wait(0.8)
    s.next_slide()
    s.play(FadeOut(VGroup(jadwal_kegiatan, header_group, target_rows, middle_nodes), scale=0.5), run_time=1.2)
