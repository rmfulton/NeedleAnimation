from manim import *
import numpy as np

class makeGrid(Scene):
    def construct(self):
        D = 1
        x = -0.3
        y = 1.4
        # theta = 0.5
        f = lambda x: 1.3
        graph = FunctionGraph(f,[0,2],YELLOW)

        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            },
            x_range=(-7.11, 7.111, 2),
            y_range=(-4,4, 2)
        )
        self.add(number_plane,graph)
