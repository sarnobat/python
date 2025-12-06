from manim import *
import random

class RemoveFirstElement(Scene):
    def construct(self):
        # Generate 4 random numbers below 100
        numbers = [random.randint(0, 99) for _ in range(4)]
        
        # Convert list to a Manim Text object
        number_text = Text(str(numbers))
        self.play(Write(number_text))
        self.wait(1)

        # Remove the first element
        numbers.pop(0)
        new_number_text = Text(str(numbers))

        # Animate the change
        self.play(Transform(number_text, new_number_text))
        self.wait(2)
