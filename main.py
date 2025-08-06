from manim import *
import random

class BSTNode(VGroup):
    def __init__(self, value, position=ORIGIN, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.circle = Circle(radius=0.3, color=BLUE, fill_opacity=0.3)
        self.text = Text(str(value), font_size=24, color=WHITE)
        self.text.move_to(self.circle.get_center())
        self.add(self.circle, self.text)
        self.move_to(position)
        
    def set_color(self, color):
        self.circle.set_color(color)

class BSTVisualization(Scene):
    def construct(self):
        # Title
        title = Text("Binary Search Tree Insertion", font_size=36, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Sample data for BST insertion
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        
        # Initialize tree structure
        tree_nodes = {}
        edges = VGroup()
        
        # Starting position for root
        root_pos = ORIGIN
        root_node = BSTNode(values[0], root_pos)
        tree_nodes[values[0]] = root_node
        
        self.play(Create(root_node))
        self.wait(0.5)
        
        # Insert remaining values
        for i, value in enumerate(values[1:], 1):
            # Find insertion position
            current = values[0]  # Start from root
            path = [current]
            
            # Simulate BST search
            while True:
                if value < current:
                    # Go left
                    if current * 2 in tree_nodes:  # Left child exists
                        current = current * 2
                        path.append(current)
                    else:
                        # Insert as left child
                        break
                else:
                    # Go right
                    if current * 2 + 1 in tree_nodes:  # Right child exists
                        current = current * 2 + 1
                        path.append(current)
                    else:
                        # Insert as right child
                        break
            
            # Calculate position for new node
            level = len(path)
            if value < current:
                # Left child
                parent_pos = tree_nodes[current].get_center()
                new_pos = parent_pos + DOWN * 1.5 + LEFT * (2 / (2 ** (level - 1)))
            else:
                # Right child
                parent_pos = tree_nodes[current].get_center()
                new_pos = parent_pos + DOWN * 1.5 + RIGHT * (2 / (2 ** (level - 1)))
            
            # Create new node
            new_node = BSTNode(value, new_pos)
            tree_nodes[value] = new_node
            
            # Create edge
            edge = Line(
                parent_pos, 
                new_pos, 
                color=WHITE, 
                stroke_width=2
            )
            edges.add(edge)
            
            # Animate insertion
            self.play(
                Create(new_node),
                Create(edge),
                run_time=0.8
            )
            
            # Highlight the path taken
            for path_value in path[:-1]:
                tree_nodes[path_value].set_color(YELLOW)
            
            self.wait(0.3)
            
            # Reset colors
            for path_value in path[:-1]:
                tree_nodes[path_value].set_color(BLUE)
            
            self.wait(0.5)
        
        # Final tree structure
        self.wait(1)
        
        # Show tree properties
        info_text = Text(
            "BST Properties:\n• Left subtree < Root\n• Right subtree > Root\n• Balanced structure",
            font_size=20,
            color=GREEN
        )
        info_text.to_edge(DOWN)
        self.play(Write(info_text))
        
        self.wait(2)

class SortingVisualization(Scene):
    def construct(self):
        # Title
        title = Text("Bubble Sort Visualization", font_size=36, color=ORANGE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create array
        numbers = [64, 34, 25, 12, 22, 11, 90]
        array_elements = []
        
        for i, num in enumerate(numbers):
            rect = Rectangle(width=0.8, height=0.8, color=BLUE, fill_opacity=0.3)
            text = Text(str(num), font_size=24)
            element = VGroup(rect, text)
            element.move_to(LEFT * 3 + RIGHT * i * 1.2)
            array_elements.append(element)
            self.play(Create(element))
        
        self.wait(0.5)
        
        # Bubble sort animation
        n = len(numbers)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Highlight current pair
                array_elements[j].set_color(YELLOW)
                array_elements[j + 1].set_color(YELLOW)
                self.wait(0.3)
                
                # Compare and swap if needed
                if numbers[j] > numbers[j + 1]:
                    # Swap numbers
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    
                    # Animate swap
                    self.play(
                        array_elements[j].animate.move_to(array_elements[j + 1].get_center()),
                        array_elements[j + 1].animate.move_to(array_elements[j].get_center()),
                        run_time=0.5
                    )
                    
                    # Update array_elements order
                    array_elements[j], array_elements[j + 1] = array_elements[j + 1], array_elements[j]
                
                # Reset colors
                array_elements[j].set_color(BLUE)
                array_elements[j + 1].set_color(BLUE)
            
            # Mark sorted element
            array_elements[n - i - 1].set_color(GREEN)
        
        self.wait(1)
        
        # Show sorted result
        result_text = Text("Array Sorted!", font_size=28, color=GREEN)
        result_text.to_edge(DOWN)
        self.play(Write(result_text))
        
        self.wait(2)

class LinkedListVisualization(Scene):
    def construct(self):
        # Title
        title = Text("Linked List Traversal", font_size=36, color=PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create linked list nodes
        values = [10, 20, 30, 40, 50]
        nodes = []
        arrows = []
        
        for i, value in enumerate(values):
            # Create node
            circle = Circle(radius=0.4, color=BLUE, fill_opacity=0.3)
            text = Text(str(value), font_size=20)
            node = VGroup(circle, text)
            node.move_to(LEFT * 4 + RIGHT * i * 2)
            nodes.append(node)
            
            # Create arrow (except for last node)
            if i < len(values) - 1:
                arrow = Arrow(
                    node.get_right(),
                    node.get_right() + RIGHT * 0.8,
                    color=WHITE,
                    buff=0.1
                )
                arrows.append(arrow)
        
        # Animate creation
        for node in nodes:
            self.play(Create(node), run_time=0.3)
        
        for arrow in arrows:
            self.play(Create(arrow), run_time=0.2)
        
        self.wait(0.5)
        
        # Traverse the list
        current = 0
        while current < len(nodes):
            # Highlight current node
            nodes[current].set_color(YELLOW)
            self.wait(0.5)
            
            # Move to next
            if current < len(nodes) - 1:
                nodes[current].set_color(GREEN)
                current += 1
            else:
                nodes[current].set_color(GREEN)
                break
        
        self.wait(1)
        
        # Show traversal info
        info_text = Text(
            "Traversal: O(n) time complexity",
            font_size=24,
            color=YELLOW
        )
        info_text.to_edge(DOWN)
        self.play(Write(info_text))
        
        self.wait(2)