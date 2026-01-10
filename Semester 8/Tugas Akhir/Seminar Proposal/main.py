from manim import *
from manim_slides import Slide
from scenes.title import title
from scenes.content import content

config.background_color = "#FAF9F6"

# Inherit dua-duanya. Urutan MovingCameraScene duluan biar aman.
class MainPresentation(MovingCameraScene, Slide):
    def construct(self):
        # --- 1. SETUP INDIKATOR ---
        self.num = Integer(1, color=GRAY, font_size=24)
        self.text_total = Text("/ 2", color=GRAY, font_size=24)
        self.ind = VGroup(self.num, self.text_total).arrange(RIGHT, buff=0.1)
        
        # Tambahkan ke layar biasa (bukan fixed)
        self.add(self.ind)

        # --- TRIK UPDATE MANUAL (PENGGANTI add_fixed...) ---
        # Ini biar indikatornya 'nempel' terus di pojok kamera walau di-zoom
        def update_posisi_indikator(mob):
            # Hitung rasio zoom saat ini
            zoom_factor = self.camera.frame.height / config.frame_height
            
            # Reset skala dulu ke 1, baru kali zoom factor (biar ukurannya visual tetap)
            mob.scale_to_fit_height(0.3 * zoom_factor) 
            
            # Tempel ke pojok kanan bawah kamera (DR = Down Right)
            # Geser dikit ke kiri atas (UL) biar gak mepet pinggir
            mob.move_to(self.camera.frame.get_corner(DR) + UL * 0.5 * zoom_factor)

        # Pasang updater-nya
        self.ind.add_updater(update_posisi_indikator)

        # --- 2. DAFTAR SLIDE ---
        urutan = [
            title,   
            content, 
        ]

        # --- 3. LOOP EKSEKUSI ---
        for i, scene_func in enumerate(urutan):
            self.num.set_value(i + 1)
            
            if i == 0: self.ind.set_opacity(0)
            else: self.ind.set_opacity(1)

            scene_func(self) 

        # Bersih-bersih
        self.ind.remove_updater(update_posisi_indikator)
        self.remove(self.ind) 
        self.play(FadeIn(Text("Selesai", color=BLACK)))