from manim import *
import random

class SubsetTree(Scene):
    def construct(self):
        # Generate 3 random numbers
        numbers = [random.randint(1, 99) for _ in range(3)]
        n = len(numbers)

        # Display the original list at the top
        number_text = Text(f"Numbers: {numbers}").scale(0.7).to_edge(UP)
        self.play(Write(number_text))
        self.wait(1)

        # Helper to create a node
        def create_node(label):
            circle = Circle(radius=0.25, color=BLUE)
            text = Text(label).scale(0.5)
            return VGroup(circle, text)

        # Compute starting Y position for the root node
        # Place it just below the list, leaving a small margin
        top_margin = 0.5
        root_y = number_text.get_bottom()[1] - 0.75

        # Recursive function to build proper binary tree
        def build_tree(nums, included=None, depth=0, x_center=0, width=6):
            if included is None:
                included = []

            # Dynamic vertical spacing to fit all levels
            total_levels = len(numbers) + 1  # including leaves
            available_height = root_y - (-3.5)  # leave some margin at bottom
            vertical_spacing = available_height / total_levels

            if not nums:
                # Leaf node shows the subset
                subset_text = Text(str(included)).scale(0.5).move_to([x_center, root_y - vertical_spacing * depth, 0])
                self.play(FadeIn(subset_text))
                return subset_text
            else:
                current = nums[0]
                rest = nums[1:]

                # Current node
                node = create_node(str(current)).move_to([x_center, root_y - vertical_spacing * depth, 0])
                self.play(FadeIn(node))

                # Left branch: include
                left_child = build_tree(rest, included + [current], depth + 1, x_center - width / 2, width / 2)
                self.play(Create(Line(node.get_bottom(), left_child.get_top())))

                # Right branch: exclude
                right_child = build_tree(rest, included, depth + 1, x_center + width / 2, width / 2)
                self.play(Create(Line(node.get_bottom(), right_child.get_top())))

                return node

        # Build the tree
        build_tree(numbers)
        self.wait(2)
