from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        circle = square
        self.play(FadeOut(circle))  # show the circle on screen

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.round_corners()
        square.next_to(circle,RIGHT)
        self.play(Create(circle), Create(square))

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle1 = Circle()
        square = Square()

        self.play(Create(square))

        self.play(square.animate.rotate(PI / 4))

        self.play(Transform(square, circle1))
        self.play(square.animate.set_fill(PINK, opacity=0.5))

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, PI), run_time = 2
        )
        self.wait()
