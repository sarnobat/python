from manim import *

class HelloWorld(Scene):
    def construct(self):
        # Create a text object
        text = Text("Hello World")
        # Display it on screen
        self.play(Write(text))
        # Keep it on screen for a moment
        self.wait(2)
