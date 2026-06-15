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
      ("Investigasi Sifat\nLatin square", C_PROC),
      ("Penarikan\nKesimpulan", C_PROC),
      ("Penulisan\nTugas Akhir", C_PROC),
      ("Selesai", C_START)
  ]
  desc_texts = [
      "", 
      r"\color{black}Mempelajari literatur aljabar max-plus dan \textit{Latin square}, memahami konsep dasar.",
      r"\color{black}Mengidentifikasi matriks \textit{Latin square} seperti apa yang dapat dikatakan komutatif.",
      r"\color{black}Investigasi mendalam kemiripan struktur dan sifat dua buah \textit{Latin square} komutatif.",
      r"\color{black}Menjawab rumusan masalah dan menarik kesimpulan dari hasil investigasi.",
      r"\color{black}Menyusun laporan tugas akhir berdasarkan hasil penelitian.",
      "" 
  ]
  nodes = VGroup()
  for i, (title, color) in enumerate(steps_data):
      if i == 0 or i == len(steps_data) - 1:
          box = Circle(
              radius=1,
              fill_color=color,
              fill_opacity=1,
              stroke_color=C_STROKE,
              stroke_width=2
          )
      else:
          box = Rectangle(
          width=3.5, height=1.5,
          fill_color=color, fill_opacity=1, stroke_color=C_STROKE, stroke_width=2
          )
      text = Text(title, font_size=20, color=TXT_COLOR, line_spacing=1).move_to(box.get_center())
      node = VGroup(box, text)
      nodes.add(node)

  nodes.arrange(RIGHT, buff=2.0)

  arrows = VGroup()
  for i in range(len(nodes) - 1):
      arrow = Arrow(
          start=nodes[i].get_right(), 
          end=nodes[i+1].get_left(), 
          color=BLACK, 
          buff=0.0, 
          max_tip_length_to_length_ratio=0.15,
          stroke_width=3
      )
      arrows.add(arrow)
  full_chart = VGroup(nodes, arrows)
  full_chart.move_to(ORIGIN)
  full_width = full_chart.width * 1.1
  s.camera.frame.move_to(full_chart.get_center())
  s.camera.frame.set(width=full_width)
  s.play(DrawBorderThenFill(nodes), Create(arrows), run_time=1)
  s.wait(0.5)
  s.camera.frame.save_state()

  def create_desc(index, node):
      deskripsi_str = desc_texts[index]
      desc_obj = Tex(
          r"\parbox{6cm}{\centering " + deskripsi_str + r"}",
          font_size=24, 
          color=BLACK,
          tex_template=my_template
      )

      is_up = (index % 2 != 0)
      if is_up:
          desc_obj.next_to(node, UP, buff=0.8)
      else:
          desc_obj.next_to(node, DOWN, buff=0.8)

      connector = Line(
          start=node.get_top() if is_up else node.get_bottom(),
          end=desc_obj.get_bottom() if is_up else desc_obj.get_top(),
          color=GRAY, stroke_width=1
      )
      return VGroup(desc_obj, connector)
  process_indices = [1, 2, 3, 4, 5]
  chunks = [process_indices[i:i + 2] for i in range(0, len(process_indices), 2)]

  current_desc_group = VGroup()
  last_visited_idx = 0 
  for chunk in chunks:
      group_mobjects = VGroup(*[nodes[i] for i in chunk])
      target_center = group_mobjects.get_center()
      target_width = group_mobjects.width * 1.3
      min_width = nodes[0].width * 4
      if target_width < min_width: target_width = min_width
      entrance_arrow = arrows[last_visited_idx]
      travel_dot = Dot(color=DOT_COLOR, radius=0.1)

      if len(current_desc_group) > 0:
          s.play(FadeOut(current_desc_group), run_time=0.3)
          current_desc_group = VGroup()
      s.play(
          s.camera.frame.animate.move_to(target_center).set(width=target_width),
          MoveAlongPath(travel_dot, entrance_arrow),
          run_time=1
      )
      s.wait(0.5)
      s.remove(travel_dot)
      for i, idx in enumerate(chunk):
          node = nodes[idx]

          if i > 0: 
              internal_arrow = arrows[idx - 1]
              internal_dot = Dot(color=DOT_COLOR, radius=0.1)
              s.play(MoveAlongPath(internal_dot, internal_arrow), run_time=1)
              s.remove(internal_dot)
          desc_grp = create_desc(idx, node)

          s.play(
              Circumscribe(node[0], color=CIRCUM_COLOR, time_width=0.75, buff=0),
              Write(desc_grp),
              run_time=1
          )

          current_desc_group.add(desc_grp)
          last_visited_idx = idx
      s.next_slide()
  if len(current_desc_group) > 0:
      s.play(FadeOut(current_desc_group), run_time=0.3)
  final_arrow = arrows[last_visited_idx]
  final_dot = Dot(color=DOT_COLOR, radius=0.1)
  s.play(
      Restore(s.camera.frame),
      MoveAlongPath(final_dot, final_arrow),
      run_time=1
  )
  s.remove(final_dot)
  s.wait(0.5)

  start_node = nodes[0]
  end_node = nodes[-1]
  middle_nodes = VGroup(*[nodes[i] for i in range(1, len(nodes)-1)])

  next_slide_count(s)
  s.play(
      FadeOut(start_node),
      FadeOut(end_node),
      FadeOut(arrows),
      middle_nodes.animate.arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=0.5).scale(0.8),
      run_time=1
  )

  def create_cell_rect(w, h, x, y):
    rect = Rectangle(width=w, height=h, stroke_color=BLACK, stroke_width=1.5)
    rect.move_to([x + w/2, y - h/2, 0])
    return rect

  TABLE_ORIGIN = UP * 2.5 + LEFT * 6
  ROW_H = 0.7
  COL_NO_W = 0.8
  COL_NAME_W = 6.5 
  COL_WEEK_W = 0.4
  BAR_COLOR = "#0072BD"

  header_group = VGroup()

  h_no_rect = create_cell_rect(COL_NO_W, ROW_H*2, TABLE_ORIGIN[0], TABLE_ORIGIN[1])
  h_no_txt = Text("NO", font_size=24, color=BLACK).move_to(h_no_rect)
  header_group.add(h_no_rect, h_no_txt)

  h_name_rect = create_cell_rect(COL_NAME_W, ROW_H*2, TABLE_ORIGIN[0] + COL_NO_W, TABLE_ORIGIN[1])
  h_name_txt = Text("NAMA KEGIATAN", font_size=24, color=BLACK).move_to(h_name_rect)
  header_group.add(h_name_rect, h_name_txt)

  total_month_w = COL_WEEK_W * 12
  h_bulan_rect = create_cell_rect(total_month_w, ROW_H, TABLE_ORIGIN[0] + COL_NO_W + COL_NAME_W, TABLE_ORIGIN[1])
  h_bulan_txt = Text("BULAN", font_size=24, color=BLACK).move_to(h_bulan_rect)
  header_group.add(h_bulan_rect, h_bulan_txt)

  curr_x = TABLE_ORIGIN[0] + COL_NO_W + COL_NAME_W
  curr_y = TABLE_ORIGIN[1] - ROW_H

  for m in range(1, 4):
      month_w = COL_WEEK_W * 4
      hm_rect = create_cell_rect(month_w, ROW_H/2, curr_x, curr_y)
      hm_txt = Text(str(m), font_size=18, color=BLACK).move_to(hm_rect)
      header_group.add(hm_rect, hm_txt)

      w_y = curr_y - ROW_H/2
      w_x = curr_x
      for w in range(1, 5):
          hw_rect = create_cell_rect(COL_WEEK_W, ROW_H/2, w_x, w_y)
          hw_txt = Text(str(w), font_size=12, color=BLACK).move_to(hw_rect)
          header_group.add(hw_rect, hw_txt)
          w_x += COL_WEEK_W
      curr_x += month_w

  tabel_data = steps_data[1:-1] 

  target_rows = VGroup()
  y_data_start = TABLE_ORIGIN[1] - (ROW_H * 2)

  for i, (title, _) in enumerate(tabel_data):
      row_y = y_data_start - (i * ROW_H)

      no_rect = create_cell_rect(COL_NO_W, ROW_H, TABLE_ORIGIN[0], row_y)
      no_txt = Text(str(i+1), font_size=20, color=BLACK).move_to(no_rect)

      name_rect = create_cell_rect(COL_NAME_W, ROW_H, TABLE_ORIGIN[0] + COL_NO_W, row_y)
      clean_title = title.replace("\n", " ")
      name_txt = Text(
          clean_title, 
          font_size=20, 
          color=BLACK, 
          t2s={"Latin square": ITALIC}
      )

      max_text_width = COL_NAME_W - 0.4 
      if name_txt.width > max_text_width:
          name_txt.scale(max_text_width / name_txt.width)

      name_txt.align_to(name_rect, LEFT).shift(RIGHT * 0.2)
      name_txt.match_y(name_rect)

      grid_group = VGroup()
      grid_x_start = TABLE_ORIGIN[0] + COL_NO_W + COL_NAME_W
      for w in range(12):
          gw_rect = create_cell_rect(COL_WEEK_W, ROW_H, grid_x_start + (w * COL_WEEK_W), row_y)
          grid_group.add(gw_rect)

      full_row = VGroup(no_rect, no_txt, name_rect, name_txt, grid_group)
      target_rows.add(full_row)
      
  jadwal_kegiatan = Title("Jadwal Kegiatan", font_size=28, color=BLACK, include_underline=True, match_underline_width_to_text=True)
  jadwal_kegiatan[1].set_color(BLACK)
  jadwal_kegiatan.move_to(header_group.get_top() + UP * 0.5)
  s.play(
      s.camera.frame.animate.move_to(header_group.get_center() + DOWN*1.5).set(width=header_group.width * 1.3),
      FadeIn(header_group), Write(jadwal_kegiatan),
      run_time=0.5
  )

  schedule_config = [
      (0, 3),
      (3, 3),
      (5, 4),
      (8, 2),
      (9, 3)
  ]

  for i in range(len(target_rows)):
      row = target_rows[i]
      s.play(Create(row[0]), Create(row[2]), Create(row[4]), run_time=0.3)
      start_idx, duration = schedule_config[i]
      bar_w = duration * COL_WEEK_W

      bar = Rectangle(
          width=bar_w, height=ROW_H,
          fill_color=BAR_COLOR, fill_opacity=1,
          stroke_color=BLACK, stroke_width=1
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
          run_time=0.5
      )

  s.wait(1)
  s.next_slide()
  s.play(
      FadeOut(Group(jadwal_kegiatan,header_group,target_rows,middle_nodes), scale=0.5),
      run_time=1.5
  )