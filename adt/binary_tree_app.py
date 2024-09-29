import tkinter as tk
from tkinter import messagebox, colorchooser

class TreeNode:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.used_roles = set()

    def insert_as_parent(self, name, role):
        if role in ["Head Coach", "Batting Coach", "Bowling Coach"] and role in self.used_roles:
            messagebox.showerror("Error", f"{role} already exists and cannot be added again.")
            return

        new_node = TreeNode(name, role)
        if self.root:
            new_node.left = self.root
        self.root = new_node
        self.used_roles.add(role)

    def insert_as_left_child(self, parent_role, name, role):
        if role in ["Head Coach", "Batting Coach", "Bowling Coach"] and role in self.used_roles:
            messagebox.showerror("Error", f"{role} already exists and cannot be added again.")
            return

        parent_node = self._find(self.root, parent_role)
        if parent_node:
            if parent_node.left is None:
                parent_node.left = TreeNode(name, role)
                self.used_roles.add(role)
            else:
                messagebox.showerror("Error", f"{parent_role} already has a left child!")
        else:
            messagebox.showerror("Error", f"{parent_role} not found!")

    def insert_as_right_child(self, parent_role, name, role):
        if role in ["Head Coach", "Batting Coach", "Bowling Coach"] and role in self.used_roles:
            messagebox.showerror("Error", f"{role} already exists and cannot be added again.")
            return

        parent_node = self._find(self.root, parent_role)
        if parent_node:
            if parent_node.right is None:
                parent_node.right = TreeNode(name, role)
                self.used_roles.add(role)
            else:
                messagebox.showerror("Error", f"{parent_role} already has a right child!")
        else:
            messagebox.showerror("Error", f"{parent_role} not found!")

    def _find(self, node, role):
        if node is None:
            return None
        if node.role == role:
            return node
        left_result = self._find(node.left, role)
        if left_result:
            return left_result
        return self._find(node.right, role)

    def delete(self, role):
        self.root = self._delete(self.root, role)
        if role in self.used_roles:
            self.used_roles.remove(role)

    def _delete(self, node, role):
        if node is None:
            return None
        if node.role == role:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.role, node.name = temp.role, temp.name
            node.right = self._delete(node.right, temp.role)
            return node
        node.left = self._delete(node.left, role)
        node.right = self._delete(node.right, role)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        return elements

    def _inorder_traversal(self, node, elements):
        if node:
            self._inorder_traversal(node.left, elements)
            elements.append(f"{node.role}: {node.name}")
            self._inorder_traversal(node.right, elements)

    def preorder_traversal(self):
        elements = []
        self._preorder_traversal(self.root, elements)
        return elements

    def _preorder_traversal(self, node, elements):
        if node:
            elements.append(f"{node.role}: {node.name}")
            self._preorder_traversal(node.left, elements)
            self._preorder_traversal(node.right, elements)

    def postorder_traversal(self):
        elements = []
        self._postorder_traversal(self.root, elements)
        return elements

    def _postorder_traversal(self, node, elements):
        if node:
            self._postorder_traversal(node.left, elements)
            self._postorder_traversal(node.right, elements)
            elements.append(f"{node.role}: {node.name}")

class BinaryTreeGUI:
    def __init__(self, root):
        self.tree = root
        self.window = tk.Tk()
        self.window.title("Indian Cricket Team Management Structure")

        # Styling
        self.window.configure(bg="light blue")

        # Layout
        self.create_widgets()
        self.canvas = tk.Canvas(self.window, bg="white", width=1500, height=800)
        self.canvas.grid(row=5, column=0, columnspan=8, pady=10, padx=10)

        # Initial draw
        self.draw_tree()

    def create_widgets(self):
        tk.Label(self.window, text="Name:", bg="light blue", font=("Arial", 13)).grid(row=0, column=0, padx=3, pady=3, sticky="e")
        self.name_entry = tk.Entry(self.window, font=("Arial", 13))
        self.name_entry.grid(row=0, column=1, padx=3, pady=3)

        tk.Label(self.window, text="Role:", bg="light blue", font=("Arial", 13)).grid(row=0, column=2, padx=3, pady=3, sticky="e")
        self.role_entry = tk.Entry(self.window, font=("Arial", 13))
        self.role_entry.grid(row=0, column=3, padx=3, pady=3)

        tk.Label(self.window, text="Predefined Roles:", bg="light blue", font=("Arial", 13)).grid(row=0, column=4, padx=3, pady=3, sticky="e")
        self.role_var = tk.StringVar(self.window)
        roles = ["Head Coach", "Batting Coach", "Bowling Coach", "Asst Batting Coach", "Asst Bowling Coach", 
                 "Jr Batting Coach", "Jr Bowling Coach", "Data Analyst", "Social Media Creator", 
                 "Batting Fitness Coach", "Asst Batting Fitness Coach", "Bowling Fitness Coach", "Asst Bowling Fitness Coach"]
        self.role_menu = tk.OptionMenu(self.window, self.role_var, *roles)
        self.role_menu.config(font=("Arial", 13))
        self.role_menu.grid(row=0, column=5, padx=3, pady=3)

        tk.Label(self.window, text="Parent Role:", bg="light blue", font=("Arial", 13)).grid(row=1, column=1, padx=3, pady=3, sticky="e")
        self.parent_role_entry = tk.Entry(self.window, font=("Arial", 13))
        self.parent_role_entry.grid(row=1, column=2, padx=3, pady=3)

        tk.Label(self.window, text="Insert as:", bg="light blue", font=("Arial", 13)).grid(row=1, column=3, padx=5, pady=5, sticky="e")
        self.insert_var = tk.StringVar(self.window)
        self.insert_var.set("Parent")
        options = ["Parent", "Left Child", "Right Child"]
        self.insert_menu = tk.OptionMenu(self.window, self.insert_var, *options)
        self.insert_menu.config(font=("Arial", 13))
        self.insert_menu.grid(row=1, column=4, padx=5, pady=5, sticky="w")

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit, bg="light green", font=("Arial", 13))
        self.submit_button.grid(row=3, column=2, padx=5, pady=5)

        self.delete_button = tk.Button(self.window, text="Delete", command=self.delete, bg="light coral", font=("Arial", 13))
        self.delete_button.grid(row=3, column=3, padx=5, pady=5)

        self.inorder_button = tk.Button(self.window, text="Inorder Traversal", command=self.show_inorder, bg="light yellow", font=("Arial", 13))
        self.inorder_button.grid(row=2, column=4, padx=5, pady=5)

        self.preorder_button = tk.Button(self.window, text="Preorder Traversal", command=self.show_preorder, bg="light blue", font=("Arial", 13))
        self.preorder_button.grid(row=2, column=2, padx=5, pady=5)

        self.postorder_button = tk.Button(self.window, text="Postorder Traversal", command=self.show_postorder, bg="light green", font=("Arial", 13))
        self.postorder_button.grid(row=2, column=3, padx=5, pady=5)

        # Exit Button
        self.exit_button = tk.Button(self.window, text="Exit", command=self.window.quit, bg="light gray", font=("Arial", 13))
        self.exit_button.grid(row=3, column=4, padx=5, pady=5)

        # Display name in the corner
        self.name_label = tk.Label(self.window, text="Abin Pillai S103", bg="white", font=("Arial", 13), anchor="e")
        self.name_label.grid(row=0, column=7, padx=10, pady=10, sticky="e")

        # Adding a menu for themes
        menu_bar = tk.Menu(self.window)
        theme_menu = tk.Menu(menu_bar, tearoff=0)
        theme_menu.add_command(label="Change Background Color", command=self.change_bg_color)
        menu_bar.add_cascade(label="Theme", menu=theme_menu)
        self.window.config(menu=menu_bar)

    def submit(self):
        name = self.name_entry.get().strip()
        role = self.role_entry.get().strip() if not self.role_var.get() else self.role_var.get()
        parent_role = self.parent_role_entry.get().strip()
        insert_as = self.insert_var.get()

        if not name or not role:
            messagebox.showerror("Error", "Name and Role are required!")
            return

        if insert_as == "Parent":
            self.tree.insert_as_parent(name, role)
        elif insert_as == "Left Child":
            self.tree.insert_as_left_child(parent_role, name, role)
        elif insert_as == "Right Child":
            self.tree.insert_as_right_child(parent_role, name, role)

        self.draw_tree()

    def delete(self):
        role = self.role_entry.get().strip()
        if not role:
            messagebox.showerror("Error", "Role is required for deletion!")
            return

        self.tree.delete(role)
        self.draw_tree()

    def draw_tree(self):
        self.canvas.delete("all")
        if self.tree.root:
            self._draw_node(self.tree.root, 750, 30, 300)

    def _draw_node(self, node, x, y, spacing):
        if node:
            self.canvas.create_text(x, y, text=f"{node.name}\n({node.role})", font=("Arial", 10))
            if node.left:
                self.canvas.create_line(x, y+20, x-spacing, y+80)
                self._draw_node(node.left, x-spacing, y+100, spacing//2)
            if node.right:
                self.canvas.create_line(x, y+20, x+spacing, y+80)
                self._draw_node(node.right, x+spacing, y+100, spacing//2)

    def show_inorder(self):
        traversal = self.tree.inorder_traversal()
        messagebox.showinfo("Inorder Traversal", "\n".join(traversal))

    def show_preorder(self):
        traversal = self.tree.preorder_traversal()
        messagebox.showinfo("Preorder Traversal", "\n".join(traversal))

    def show_postorder(self):
        traversal = self.tree.postorder_traversal()
        messagebox.showinfo("Postorder Traversal", "\n".join(traversal))

    def change_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.window.configure(bg=color)
            self.name_label.configure(bg=color)

if __name__ == "__main__":
    bt = BinaryTree()
    gui = BinaryTreeGUI(bt)
    gui.window.mainloop()
