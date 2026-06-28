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
      ("Penyusunan algoritma\nLatin square komutatif", C_PROC),
      ("Penarikan\nKesimpulan", C_PROC),
      ("Penulisan\nTugas Akhir", C_PROC),
      ("Selesai", C_START)
  ]
  desc_texts = [
      "", 
      r"\color{black}Mempelajari literatur aljabar max-plus dan \textit{Latin square}, memahami konsep dasar.",
      r"\color{black}Mengidentifikasi matriks \textit{Latin square} seperti apa yang dapat dikatakan komutatif.",
      r"\color{black}Investigasi mendalam kemiripan struktur dan sifat dua buah \textit{Latin square} komutatif.",
      r"\color{black}Mengembangkan algoritma untuk menghasilkan \textit{Latin square} komutatif.",
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
  process_indices = [1, 2, 3, 4, 5, 6]
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

  s.play(
      FadeOut(start_node),
      FadeOut(end_node),
      FadeOut(arrows),
      FadeOut(middle_nodes),
      run_time=1
  )