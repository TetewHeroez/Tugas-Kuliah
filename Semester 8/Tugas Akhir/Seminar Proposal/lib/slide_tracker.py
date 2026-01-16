from manim import *

def next_slide_count(s):
  s.play(s.slide_tracker.animate.increment_value(1))