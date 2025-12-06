from manim import *
import random
from collections import deque

class SubsetTreeBFS(Scene):
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

        # Layout
        total_levels = n + 1
        root_y = number_text.get_bottom()[1] - 0.75
        available_height = root_y - (-3.5)
        vertical_spacing = available_height / total_levels
        width = 6

        # BFS queue: (node, depth, x_center, subset_so_far, next_index)
        queue = deque()
        # Start with virtual root
        queue.append((None, 0, 0, [], 0))

        while queue:
            parent_node, depth, x_center, subset, idx = queue.popleft()
            if idx >= n:
                # Leaf node: show subset
                leaf_text = Text(str(subset)).scale(0.5).move_to([x_center, root_y - vertical_spacing * depth, 0])
                self.play(FadeIn(leaf_text))
                continue

            current_num = numbers[idx]
            # Current node
            node = create_node(str(current_num)).move_to([x_center, root_y - vertical_spacing * depth, 0])
            self.play(FadeIn(node))

            if parent_node is not None:
                # Connect to parent
                line = Line(parent_node.get_bottom(), node.get_top())
                self.play(Create(line))

            # Horizontal offset
            h_offset = width / (2 ** (depth + 1))

            # Left child: include
            left_x = x_center - h_offset
            queue.append((node, depth + 1, left_x, subset + [current_num], idx + 1))
            # Right child: exclude
            right_x = x_center + h_offset
            queue.append((node, depth + 1, right_x, subset, idx + 1))

        self.wait(2)
