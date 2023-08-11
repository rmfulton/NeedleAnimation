from manim import *
import numpy as np

class makeGrid(Scene):
    def construct(self):
        scale = 3
        D = 1
        x = -0.3
        y = 1.4
        # theta = 0.5
        f = lambda x: 1.3
        graph = FunctionGraph(f,[-0.2, scale - 0.2],YELLOW)

        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            },
            x_range=(-7.11, 7.111, scale),
            y_range=(-4,4, scale)
        )
        self.add(number_plane,graph)
        self.wait(0.5)
        self.play(Rotate(graph, 2*PI), run_time=4)
        self.wait(0.5)
