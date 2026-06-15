from manim import *

def next_slide_count(scene):
    if hasattr(scene, "num"):
        val_sekarang = int(scene.num.get_value())
        val_baru = val_sekarang + 1
        
        scene.play(
            ChangeDecimalToValue(scene.num, val_baru),
            run_time=0.1
        )
        scene.wait(0.1)