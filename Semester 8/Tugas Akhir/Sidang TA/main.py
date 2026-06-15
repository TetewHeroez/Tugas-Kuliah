from manim import *
from manim_slides import Slide

from scenes.judul import *
from scenes.content import *
from scenes.pendahuluan import *
from scenes.tinjauan_pustaka import *
from scenes.metodologi import *
from scenes.penutup import *

from lib.slide_tracker import *

config.background_color = "#EAEAEA"

class MainPresentation(MovingCameraScene, Slide):
    def construct(self):
        self.total_slides = 12

        self.num = Integer(1, color=GRAY, font_size=24)
        self.text_total = Text(f"/{self.total_slides}", color=GRAY, font_size=24)
        
        self.ind = VGroup(self.num, self.text_total).arrange(RIGHT, buff=0.1).set_z_index(1000)
        
        self.logo_its = SVGMobject("assets/ITS.svg")
        self.logo_matematika = SVGMobject("assets/M.svg").next_to(self.logo_its, RIGHT, buff=0.1)
        self.logo = VGroup(self.logo_its, self.logo_matematika).arrange(RIGHT, buff=0.5).set_z_index(1000)

        def update_posisi_logo(mob):
            factor = self.camera.frame.height / config.frame_height
            mob.scale_to_fit_height(0.5 * factor)
            mob.move_to(self.camera.frame.get_corner(DL) + (UR + 0.5*RIGHT) * 0.5 * factor)
            mob.set_stroke(width=1 * factor)

        def update_posisi_angka(mob):
            factor = self.camera.frame.height / config.frame_height
            mob.scale_to_fit_height(0.3 * factor)
            mob.move_to(self.camera.frame.get_corner(DR) + UL * 0.5 * factor)

        self.logo.add_updater(update_posisi_logo)
        self.ind.add_updater(update_posisi_angka)

        urutan = [
            content,
            lambda s: zoom_section(s,1),
            pendahuluan,
            lambda s: unzoom_section(s,1),
            content,
            lambda s: zoom_section(s,2),
            tinjauan_pustaka,
            lambda s: unzoom_section(s,2),
            content,
            lambda s: zoom_section(s,3),
            metodologi,
        ]

        judul(self)
        self.play(Write(VGroup(self.logo, self.ind)), run_time=0.2)
        for scene_func in urutan:
            scene_func(self)

        self.logo.remove_updater(update_posisi_logo)
        self.ind.remove_updater(update_posisi_angka)
        
        penutup(self)