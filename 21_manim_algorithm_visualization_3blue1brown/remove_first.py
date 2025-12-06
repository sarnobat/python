from manim import *
import random

class RemoveFirstElement(Scene):
    def construct(self):
        # Generate 4 random numbers
        numbers = [random.randint(0, 99) for _ in range(4)]

        # Create Text objects for each number
        number_mobs = [Text(str(n)) for n in numbers]

        # Arrange numbers horizontally with spacing
        for i, mob in enumerate(number_mobs):
            mob.next_to(number_mobs[i - 1], RIGHT, buff=0.5) if i > 0 else mob.to_edge(LEFT)

        # Group them for easy manipulation
        number_group = VGroup(*number_mobs)
        self.play(Write(number_group))
        self.wait(1)

        # Animate removing the first number
        first_number = number_mobs[0]
        remaining_numbers = VGroup(*number_mobs[1:])
        
        # Move remaining numbers to take the first number's place
        self.play(
            first_number.animate.fade(1),                 # fade out the first number
            remaining_numbers.animate.shift(LEFT*first_number.width + LEFT*0.5)  # shift left
        )
        self.wait(2)
