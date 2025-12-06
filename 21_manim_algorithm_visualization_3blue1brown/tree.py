from manim import *
import random

class SubsetTree(Scene):
    def construct(self):
        # Generate 3 random numbers
        numbers = [random.randint(1, 99) for _ in range(3)]

        # Display the original list
        number_text = Text(f"Numbers: {numbers}").to_edge(UP)
        self.play(Write(number_text))
        self.wait(1)

        # Create nodes for binary tree
        # Level 0 (root)
        root = Circle(radius=0.4, color=BLUE)
        root_text = Text("Start").scale(0.5)
        root_group = VGroup(root, root_text).move_to(ORIGIN)
        self.play(FadeIn(root_group))

        # Level 1
        left1 = Circle(radius=0.4, color=GREEN).shift(LEFT*3 + DOWN*2)
        right1 = Circle(radius=0.4, color=GREEN).shift(RIGHT*3 + DOWN*2)
        left1_text = Text(f"Include {numbers[0]}").scale(0.5)
        right1_text = Text(f"Exclude {numbers[0]}").scale(0.5)
        left1_group = VGroup(left1, left1_text)
        right1_group = VGroup(right1, right1_text)

        # Level 2
        # Left branch of Level 1
        left2 = Circle(radius=0.4, color=ORANGE).shift(LEFT*4 + DOWN*4)
        right2 = Circle(radius=0.4, color=ORANGE).shift(LEFT*2 + DOWN*4)
        left2_text = Text(f"Include {numbers[1]}").scale(0.5)
        right2_text = Text(f"Exclude {numbers[1]}").scale(0.5)
        left2_group = VGroup(left2, left2_text)
        right2_group = VGroup(right2, right2_text)

        # Right branch of Level 1
        left3 = Circle(radius=0.4, color=ORANGE).shift(RIGHT*2 + DOWN*4)
        right3 = Circle(radius=0.4, color=ORANGE).shift(RIGHT*4 + DOWN*4)
        left3_text = Text(f"Include {numbers[1]}").scale(0.5)
        right3_text = Text(f"Exclude {numbers[1]}").scale(0.5)
        left3_group = VGroup(left3, left3_text)
        right3_group = VGroup(right3, right3_text)

        # Level 3 (leaves)
        leaves = []
        # Left-Left branch (Include first, Include second)
        leaves.append(Text(f"{numbers[0]}, {numbers[1]}, {numbers[2]}").scale(0.5).move_to(LEFT*5 + DOWN*6))
        leaves.append(Text(f"{numbers[0]}, {numbers[1]}").scale(0.5).move_to(LEFT*3 + DOWN*6))
        # Left-Right branch (Include first, Exclude second)
        leaves.append(Text(f"{numbers[0]}, {numbers[2]}").scale(0.5).move_to(LEFT*1 + DOWN*6))
        leaves.append(Text(f"{numbers[0]}").scale(0.5).move_to(RIGHT*1 + DOWN*6))
        # Right-Left branch (Exclude first, Include second)
        leaves.append(Text(f"{numbers[1]}, {numbers[2]}").scale(0.5).move_to(RIGHT*3 + DOWN*6))
        leaves.append(Text(f"{numbers[1]}").scale(0.5).move_to(RIGHT*5 + DOWN*6))
        # Right-Right branch (Exclude first, Exclude second)
        leaves.append(Text(f"{numbers[2]}").scale(0.5).move_to(RIGHT*7 + DOWN*6))
        leaves.append(Text(f"∅").scale(0.5).move_to(RIGHT*9 + DOWN*6))

        # Draw Level 1
        self.play(FadeIn(left1_group), FadeIn(right1_group))
        self.play(Create(Line(root.get_bottom(), left1.get_top())), Create(Line(root.get_bottom(), right1.get_top())))
        self.wait(0.5)

        # Draw Level 2
        self.play(FadeIn(left2_group), FadeIn(right2_group), FadeIn(left3_group), FadeIn(right3_group))
        self.play(
            Create(Line(left1.get_bottom(), left2.get_top())),
            Create(Line(left1.get_bottom(), right2.get_top())),
            Create(Line(right1.get_bottom(), left3.get_top())),
            Create(Line(right1.get_bottom(), right3.get_top()))
        )
        self.wait(0.5)

        # Draw leaves
        for leaf in leaves:
            self.play(FadeIn(leaf))
        self.wait(2)
