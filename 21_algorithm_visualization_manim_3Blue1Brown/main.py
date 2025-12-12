from manim import *

class BubbleSort(Scene):
    def construct(self):
        arr = [3, 1, 4, 2]
        dots = VGroup(*[Dot().shift(RIGHT * i) for i in range(len(arr))])
        self.play(Create(dots))
        self.play(dots[0].animate.shift(UP), dots[1].animate.shift(DOWN))
