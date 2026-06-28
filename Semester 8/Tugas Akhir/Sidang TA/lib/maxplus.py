from manim import *

# Class ini mewarisi Scene, tapi tujuannya cuma menyediakan fungsi
class MaxPlusAnim(Scene):
  def animate_maxplus_multiplication(self, m1_data, m2_data):
      # 1. Validasi
      rows_a = len(m1_data)
      cols_a = len(m1_data[0])
      rows_b = len(m2_data)
      cols_b = len(m2_data[0])
      if cols_a != rows_b:
          self.add(Text("Dimensi Error").set_color(RED))
          return
      # 2. Hitung Hasil (Logika Max-Plus)
      res_data = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
      for i in range(rows_a):
          for j in range(cols_b):
              candidates = []
              for k in range(cols_a):
                  val = m1_data[i][k] + m2_data[k][j]
                  candidates.append(val)
              res_data[i][j] = max(candidates)
      # 3. Setup Visual
      mat_a = IntegerMatrix(m1_data).set_color(BLUE)
      mat_b = IntegerMatrix(m2_data).set_color(GREEN)
      mat_res = IntegerMatrix(res_data).set_color(YELLOW)
      times_sym = MathTex(r"\otimes", font_size=60).set_color(RED)
      equals_sym = MathTex(r"=", font_size=60)
      equation = VGroup(mat_a, times_sym, mat_b, equals_sym, mat_res)
      equation.arrange(RIGHT, buff=0.5)
      
      if equation.width > config.frame_width - 1:
          equation.scale_to_fit_width(config.frame_width - 1)
      for entry in mat_res.get_entries():
          entry.set_opacity(0)
      # Intro yang lebih santai
      self.play(Write(mat_a), run_time=1)
      self.play(Write(times_sym), Write(mat_b), Write(equals_sym), run_time=1)
      self.play(Create(mat_res.get_brackets()), run_time=1)
      self.wait(1) # Jeda sebelum mulai hitung
      # 4. LOOP UTAMA
      for r in range(rows_a):
          for c in range(cols_b):
              # --- A. Highlight Baris & Kolom (Diperlambat) ---
              row_obj = mat_a.get_rows()[r]
              col_obj = mat_b.get_columns()[c]
              rect_row = SurroundingRectangle(row_obj, color=BLUE, buff=0.1)
              rect_col = SurroundingRectangle(col_obj, color=GREEN, buff=0.1)
              self.play(Create(rect_row), Create(rect_col), run_time=1.0) # Diperlambat jadi 1 detik
              
              # --- B. Buat String Perhitungan ---
              parts_str = []
              sums_val = []
              for k in range(cols_a):
                  val_a = m1_data[r][k]
                  val_b = m2_data[k][c]
                  s = val_a + val_b
                  sums_val.append(s)
                  parts_str.append(f"({val_a}+{val_b})")
              max_val = max(sums_val)
              inner_content = ", ".join(parts_str)
              # Rumus lengkap
              latex_str = f"\\max \\big( {inner_content} \\big) = {max_val}"
              
              step_calculation = MathTex(latex_str, font_size=34).next_to(equation, DOWN, buff=0.7)
              step_calculation[-len(str(max_val)):].set_color(YELLOW)
              # Animasi menulis rumus (Sangat diperlambat agar terbaca)
              self.play(Write(step_calculation), run_time=1.0)
              
              # *** JEDA PENTING ***: Biarkan penonton membaca rumus
              self.wait(0.5)
              # --- C. Pindahkan Hasil ke Matriks ---
              entry_index = r * cols_b + c
              target_entry = mat_res.get_entries()[entry_index]
              source_part = step_calculation[-len(str(max_val)):] 
              
              # Transformasi diperlambat
              self.play(
                  ReplacementTransform(source_part, target_entry),
                  target_entry.animate.set_opacity(1),
                  run_time=1
              )
              
              # *** JEDA PENTING ***: Biarkan penonton melihat hasil masuk
              self.wait(0.5)
              # --- D. Cleanup ---
              self.play(
                  FadeOut(rect_row),
                  FadeOut(rect_col),
                  FadeOut(step_calculation),
                  run_time=0.5
              )
      self.play(Indicate(mat_res, color=YELLOW, scale_factor=1.1), run_time=1)
      self.wait(2)