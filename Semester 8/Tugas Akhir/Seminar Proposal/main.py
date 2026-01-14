from manim import *
from manim_slides import Slide

from scenes.title import title
from scenes.content import *
from scenes.pendahuluan import *

from lib.bibtex_system import *

config.background_color =  "#EAEAEA"

class MainPresentation(MovingCameraScene, Slide):
    def construct(self):
        urutan = [
            # title,   
            # content,
            # lambda s: zoom_section(s,1),
            pendahuluan,
            # lambda s: unzoom_section(s,1),
            # content,
            # lambda s: zoom_section(s,2)
        ]

        self.total_slides = 5
        self.slide_tracker = ValueTracker(0)

        def next_slide_count(self):
            self.play(self.slide_tracker.animate.increment_value(1))
        
        self.num = Integer(self.slide_tracker.get_value(), color=GRAY, font_size=24)
        self.text_total = Text(f"/{self.total_slides}", color=GRAY, font_size=24)
        self.logo_its = SVGMobject("assets/ITS.svg")
        self.logo_matematika = SVGMobject("assets/M.svg").next_to(self.logo_its, RIGHT, buff=0.1)
        self.logo = VGroup(self.logo_its, self.logo_matematika).arrange(RIGHT, buff=0.5).set_z_index(1000)
        self.ind = VGroup(self.num, self.text_total).arrange(RIGHT, buff=0.1).set_z_index(1000)

        def update_posisi_indikator(mob, corner, padding, height=0.3):
            zoom_factor = self.camera.frame.height / config.frame_height
            mob.scale_to_fit_height(height * zoom_factor) 
            mob.move_to(self.camera.frame.get_corner(corner) + (padding) * 0.5 * zoom_factor)

        self.ind.add_updater(lambda m: update_posisi_indikator(m, DR, UL))
        self.logo.add_updater(lambda m: update_posisi_indikator(m, DL, UR+0.5*RIGHT, 0.5))

        for i, scene_func in enumerate(urutan):
            self.num.set_value(i + 1)
            if i == 1: 
                self.play(Write(self.logo),Write(self.ind), run_time=1)
            scene_func(self) 
            next_slide_count(self)

        self.ind.remove_updater(update_posisi_indikator)
        self.remove(self.ind) 
        uncreate_content(self)
        self.play(FadeIn(Text("Selesai", color=BLACK)))