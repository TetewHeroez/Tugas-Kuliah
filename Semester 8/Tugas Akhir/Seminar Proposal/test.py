from manim import *

config.background_color = WHITE

class MaxPlusMatrixCalcFinal(Scene):
    def construct(self):
        # --- KONFIGURASI KECEPATAN ---
        # 0.5 = 2x lebih cepat
        speed = 0.5 
        
        # --- 1. SETUP DATA & LOGIKA HITUNG ---
        matrix_A = [[2, 3], [4, 1]]
        matrix_B = [[1, 5], [2, 3]]
        
        rows_a, cols_a = len(matrix_A), len(matrix_A[0])
        rows_b, cols_b = len(matrix_B), len(matrix_B[0])

        # Hitung hasil (Logic)
        res_data = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                candidates = []
                for k in range(cols_a):
                    val = matrix_A[i][k] + matrix_B[k][j]
                    candidates.append(val)
                res_data[i][j] = max(candidates)

        # --- 2. SETUP VISUAL (STATIC / LANGSUNG MUNCUL) ---
        
        # A. Judul (Pastikan Hitam)
        judul_bab = Title("Perkalian Matriks Max-Plus", color=BLACK)
        judul_bab[1].set_color(BLACK) # Garis bawah hitam
        
        # B. Rumus (Langsung di posisi Kiri) - Text Hitam
        rumus_1 = MathTex(r"(A \otimes B)_{ij}", color=BLACK, font_size=30)
        rumus_2 = MathTex(r"= \max_{1 \leq k \leq n} (a_{ik} + b_{kj})", color=BLACK, font_size=30)
        
        # Posisi Rumus
        rumus_2.next_to(rumus_1, RIGHT, buff=0.1)
        rumus_group = VGroup(rumus_1, rumus_2)
        
        kotak_rumus = SurroundingRectangle(
            rumus_group,
            color=BLUE_D,
            fill_color=BLUE_D,
            fill_opacity=0.6,
            corner_radius=0,
            buff=0.3
        ).set_z_index(-1)
        
        full_rumus = VGroup(kotak_rumus, rumus_group)
        full_rumus.to_edge(LEFT, buff=1.0).shift(UP*0.5)

        # C. Matriks Definisi (Langsung di posisi Kanan Rumus) - Set Warna HITAM
        mat_a = IntegerMatrix(matrix_A).set_color(BLACK)
        mat_b = IntegerMatrix(matrix_B).set_color(BLACK)
        
        label_a = MathTex("A =", font_size=30, color=BLACK)
        label_b = MathTex("B =", font_size=30, color=BLACK)
        
        group_a = VGroup(label_a, mat_a.scale(0.6)).arrange(RIGHT, buff=0.2)
        group_b = VGroup(label_b, mat_b.scale(0.6)).arrange(RIGHT, buff=0.2)
        
        # Susun group a dan b
        group_a.next_to(full_rumus, RIGHT, buff=1.0)
        group_b.next_to(group_a, RIGHT, buff=0.5)
        
        kotak_group_a_b = SurroundingRectangle(
            VGroup(group_a, group_b),
            color=GREEN_D,
            fill_color=GREEN_D,
            fill_opacity=0.6,
            corner_radius=0,
            buff=0.2
        ).set_z_index(-1)

        # --- TAMPILKAN OBJEK AWAL SECARA INSTAN ---
        self.add(judul_bab)
        self.add(full_rumus)
        self.add(kotak_group_a_b, group_a, group_b)
        
        self.wait(1 * speed)

        # --- 3. MULAI ANIMASI PERHITUNGAN ---

        # Persiapan Transisi ke Bentuk Persamaan Besar
        # Copy dan pastikan WARNA HITAM
        target_mat_a = mat_a.copy().scale(2).set_color(BLACK) 
        target_mat_b = mat_b.copy().scale(2).set_color(BLACK)

        # Matriks Hasil (Kosong/Transparan tapi bracket Hitam)
        mat_res = IntegerMatrix(res_data).set_color(BLACK)
        target_mat_res = mat_res.copy().scale(1.2) 
        target_mat_res.get_entries().set_opacity(0) # Sembunyikan angka dulu
        target_mat_res.set_color(BLACK) # Bracket hitam
        target_mat_res.match_height(target_mat_a)

        times_sym = MathTex(r"\otimes", font_size=60, color=BLACK)
        equals_sym = MathTex(r"=", font_size=60, color=BLACK)

        # Group Akhir (Posisi Bawah)
        group_akhir = VGroup(
            target_mat_a, 
            times_sym, 
            target_mat_b, 
            equals_sym, 
            target_mat_res
        )
        group_akhir.arrange(RIGHT, buff=0.3)
        group_akhir.move_to(DOWN * 1.5)

        # Animasi Transisi: Dari Definisi Kecil ke Persamaan Besar
        self.play(
            ReplacementTransform(group_a[1].copy(), target_mat_a), 
            ReplacementTransform(group_b[1].copy(), target_mat_b), 
            Write(times_sym),
            Write(equals_sym),
            Write(target_mat_res.get_brackets()), 
            run_time=1.5 * speed
        )
        self.wait(0.5 * speed)

        # Referensi ulang untuk loop
        final_mat_a = target_mat_a
        final_mat_b = target_mat_b
        final_mat_res = target_mat_res

        # --- 4. LOOP PERHITUNGAN ---
        for r in range(rows_a):
            for c in range(cols_b):
                row_obj = final_mat_a.get_rows()[r]
                col_obj = final_mat_b.get_columns()[c]
                
                # Highlight Baris & Kolom (Warna cerah agar terlihat di putih)
                rect_row = SurroundingRectangle(row_obj, color=BLUE, buff=0.1)
                rect_col = SurroundingRectangle(col_obj, color=GREEN, buff=0.1)
                
                self.play(Create(rect_row), Create(rect_col), run_time=0.4 * speed)

                # Siapkan Teks Perhitungan
                parts_str = []
                sums_val = []
                for k in range(cols_a):
                    val_a = matrix_A[r][k]
                    val_b = matrix_B[k][c]
                    val_sum = val_a + val_b
                    sums_val.append(val_sum)
                    parts_str.append(f"({val_a}+{val_b})")
                
                max_val = max(sums_val)
                inner_content = ", ".join(parts_str)
                latex_str = f"\\max \\big( {inner_content} \\big) = {max_val}"
                
                # Tampilkan Teks di Bawah (Warna Coklat Tua agar kontras)
                step_calculation = MathTex(latex_str, font_size=34, color=DARK_BROWN)
                step_calculation.next_to(group_akhir, DOWN, buff=0.3)

                self.play(Write(step_calculation), run_time=0.6 * speed)
                self.wait(0.3 * speed)

                # Isi Angka ke Matriks Hasil
                entry_index = r * cols_b + c
                target_placeholder = final_mat_res.get_entries()[entry_index]
                
                # Angka hasil berwarna HITAM
                new_entry = MathTex(str(max_val), font_size=target_placeholder.font_size, color=BLACK)
                new_entry.move_to(target_placeholder.get_center())
                
                # Ambil bagian angka terakhir dari teks perhitungan
                source_part = step_calculation[-len(str(max_val)):] 
                
                self.play(
                    ReplacementTransform(source_part.copy(), new_entry), 
                    run_time=0.6 * speed
                )

                # Bersihkan Highlight & Teks
                self.play(
                    FadeOut(rect_row),
                    FadeOut(rect_col),
                    FadeOut(step_calculation),
                    run_time=0.3 * speed
                )

        # Highlight Hasil Akhir (Warna Merah Bata / Coklat)
        self.play(Indicate(final_mat_res, color=DARK_BROWN, scale_factor=1.1), run_time=1 * speed)
        self.wait(2 * speed)