import tkinter as tk
from tkinter import messagebox
from tree import Tree
from node import Node

class BinaryTreeApp:
    def __init__(self, root):
        self.tree = Tree()
        self.root = root
        self.root.title("Binary Tree GUI")
        
        self.canvas_width = 600
        self.canvas_height = 400

        # Create canvas for drawing the tree
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.create_widgets()

    def create_widgets(self):
        # Input field for adding nodes
        self.label = tk.Label(self.root, text="Enter a value to add to the tree:")
        self.label.grid(row=1, column=0)

        self.input_value = tk.Entry(self.root)
        self.input_value.grid(row=1, column=1)

        # Add button
        self.add_button = tk.Button(self.root, text="Add Node", command=self.add_node)
        self.add_button.grid(row=1, column=2)

        # Search button
        self.search_button = tk.Button(self.root, text="Search Node", command=self.search_node)
        self.search_button.grid(row=2, column=2)

        # Display the tree button
        self.display_button = tk.Button(self.root, text="Display Tree", command=self.display_tree)
        self.display_button.grid(row=3, column=2)

        # Delete tree button
        self.delete_button = tk.Button(self.root, text="Delete Tree", command=self.delete_tree)
        self.delete_button.grid(row=4, column=2)

        # Output display area
        self.output_text = tk.Text(self.root, width=40, height=10)
        self.output_text.grid(row=5, column=0, columnspan=3)

    def add_node(self):
        value = self.input_value.get()
        if value.isdigit():
            self.tree.add(int(value))
            self.output_text.insert(tk.END, f"Node {value} added successfully.\n")
            self.display_tree()  # Redraw the tree when a node is added
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
        self.input_value.delete(0, tk.END)

    def search_node(self):
        value = self.input_value.get()
        if value.isdigit():
            result = self.tree.find(int(value))
            if result:
                self.output_text.insert(tk.END, f"Node {value} found.\n")
            else:
                self.output_text.insert(tk.END, f"Node {value} not found.\n")
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
        self.input_value.delete(0, tk.END)

    def display_tree(self):
        # Clear the canvas before drawing the new tree
        self.canvas.delete("all")
        
        if self.tree.getRoot() is not None:
            # Start the recursive drawing from the root node
            self.draw_tree(self.tree.getRoot(), self.canvas_width // 2, 30, 100)
        else:
            self.output_text.insert(tk.END, "Tree is empty.\n")

    def draw_tree(self, node, x, y, dx):
        if node is not None:
            # Draw the node
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.data))
            
            # Draw the left and right children if they exist
            if node.left is not None:
                # Draw the edge to the left child
                self.canvas.create_line(x, y + 20, x - dx, y + 80, arrow=tk.LAST)
                # Recursively draw the left child
                self.draw_tree(node.left, x - dx, y + 80, dx // 2)

            if node.right is not None:
                # Draw the edge to the right child
                self.canvas.create_line(x, y + 20, x + dx, y + 80, arrow=tk.LAST)
                # Recursively draw the right child
                self.draw_tree(node.right, x + dx, y + 80, dx // 2)

    def delete_tree(self):
        self.tree.deleteTree()
        self.canvas.delete("all")
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Tree deleted.\n")


if __name__ == "__main__":
    window = tk.Tk()
    app = BinaryTreeApp(window)
    window.mainloop()
