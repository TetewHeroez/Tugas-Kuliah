from manim import *

def header(s):
    # --- JUDUL HEADER ---
    # Menggunakan Tex untuk font Serif (mirip LaTeX)
    title = Tex(r"\textit{Low-Thrust Optimal Escape Trajectories}", font_size=34)
    author = Tex(r"Luigi Mascolo", font_size=34)
    # Posisi
    title.to_corner(UL, buff=0.5)
    author.to_corner(UR, buff=0.5)
    # Garis Header
    line = Line(start=LEFT_SIDE, end=RIGHT_SIDE, stroke_width=2, color=GRAY)
    line.next_to(title, DOWN, buff=0.2)
    
    # Tambahkan ke layar
    s.add(title, author, line)

def footer(s):
    # --- PROGRESS BAR (Rocket) ---
    
    # 1. Garis Track (Jalur roket)
    track_line = Line(start=LEFT_SIDE * 0.9, end=RIGHT_SIDE * 0.9, color=GREEN_E, stroke_width=10)
    track_line.to_edge(DOWN, buff=0.5)
    
    # Hiasan garis tipis di dalam (opsional, biar mirip gambar)
    inner_line = Line(start=LEFT_SIDE * 0.9, end=RIGHT_SIDE * 0.9, color=GREEN_B, stroke_width=2)
    inner_line.move_to(track_line)
    # 2. Ikon Roket
    # Kalau punya file SVG: rocket = SVGMobject("rocket.svg").scale(0.5)
    # Di sini saya pakai Triangle sbg placeholder roket
    rocket = Triangle(color=WHITE, fill_opacity=1).rotate(-90*DEGREES).scale(0.2)
    
    # 3. Logika Pergerakan (ValueTracker)
    # Ini 'variabel' yang menyimpan progress (0 = awal, 1 = akhir)
    s.progress_tracker = ValueTracker(0)
    # 4. Updater (Sihir-nya di sini)
    # Fungsi ini akan dipanggil setiap frame untuk menempelkan roket ke garis sesuai nilai tracker
    def update_rocket(mob):
        # Ambil nilai 0 s/d 1
        alpha = s.progress_tracker.get_value()
        # Pindahkan roket ke titik koordinat garis sesuai persentase alpha
        mob.move_to(track_line.point_from_proportion(alpha))
    
    rocket.add_updater(update_rocket)
    # 5. Teks Footer Kiri Bawah
    footer_text = Text("Luigi Mascolo Ph.D. thesis defense", font_size=18, weight=BOLD)
    footer_text.next_to(track_line, DOWN, buff=0.2).to_edge(LEFT, buff=1)
    s.add(track_line, inner_line, rocket, footer_text)