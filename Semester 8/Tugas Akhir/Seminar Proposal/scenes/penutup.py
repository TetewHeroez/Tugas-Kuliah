from manim import *

def penutup(s):
      thanks = Text("Terima Kasih!", font_size=64, color=BLACK)
      powered_by = Text("Powered by Manim CE", font_size=24, color=GRAY).move_to(ORIGIN+RIGHT*3+DOWN)
      banner = ManimBanner(dark_theme=False).scale(0.2)
      banner.next_to(powered_by, RIGHT, buff=0.2)
      reference_box = Rectangle(
          width=config.frame_width/2,
          height=config.frame_height,
          fill_color=BLACK,
          fill_opacity=1,
          stroke_width=0
      ).to_edge(LEFT, buff=0)
      if s.mobjects:
          s.play(FadeOut(Group(*s.mobjects)),s.camera.frame.animate.move_to(ORIGIN).set(height=config.frame_height), run_time=0.2)
      reference_box = Rectangle(
          width=config.frame_width / 2,
          height=config.frame_height,
          fill_color=BLACK,
          fill_opacity=1,
          stroke_width=0
      ).to_edge(LEFT, buff=0)
      cit_style = {"font_size": 17, "color": WHITE} 
      lbl_ref = Text("Referensi:", font_size=24, weight=BOLD, color=WHITE)
      ref1 = Text("Allhunalifah, A., & Sergeev, S. (2024b). On a security of the\nmodifying the tropical version of stickel’s key exchange\nprotocol", **cit_style)   
      ref2 = Text("Mufid, M. S., & Subiono. Eigenvectors of latin squares in\nalgebra.", **cit_style)
      ref3 = Text("Subiono. (2015). Aljabar min-max plus dan terapannya.", **cit_style) 
      ref4 = Text("Subiono. (2022). Aljabar: Suatu pondasi matematika.", **cit_style)
      ref5 = Text("Zufar, M. Z. (2023). Konstruksi grup latin square pada\naljabar max-plus.", **cit_style)
      ref6 = Text("George, W. D., John Clay; Wallis. (2017). Introduction\nto combinatorics (2nd ed.).", **cit_style)
      ref7 = Text("Huang, H., Jiang, X., Peng, C., & Pan, G. (2024). A new\nsemiring and its cryptographic applications.", **cit_style)
      citations = VGroup(lbl_ref, ref1, ref6, ref7, ref2, ref3, ref4, ref5).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
      citations.move_to(reference_box.get_center()).shift(LEFT * 0.2)
      
      s.play(Write(thanks), run_time=1)
      s.wait(2)
      s.play(FadeIn(reference_box),
                thanks.animate.to_edge(RIGHT, buff=1),
                Write(powered_by),
                LaggedStart(
              *[FadeIn(mob, shift=UP*0.5) for mob in citations], 
              lag_ratio=0.2),
                banner.create(),
                run_time=1)
      s.wait(1)