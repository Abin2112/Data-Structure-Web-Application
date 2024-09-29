import tkinter as tk
from tkinter import simpledialog, messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def delete_at_position(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for _ in range(position - 1):
            temp = temp.next
            if temp is None or temp.next is None:
                raise IndexError("Position out of bounds.")
        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

    def display_list(self):
        temp = self.head
        if temp is None:
            return "Linked List is empty."
        linked_list_str = ""
        while temp:
            linked_list_str += str(temp.data) + ", "
            temp = temp.next
        return linked_list_str[:-2]  

class LinkedListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.linked_list = LinkedList()
        self.title("Singly Linked List Operations GUI")
        self.geometry("900x700")
        self.configure(bg='#0a043c')
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Singly Linked List Operations", font=("Helvetica", 24, "bold"), fg="#f3ffbd", bg='#0a043c')
        self.title_label.pack(pady=20)

        self.list_label = tk.Label(self, text=self.linked_list.display_list(), font=("Helvetica", 18), fg="#f3ffbd", bg='#0a043c')
        self.list_label.pack(pady=20)

        button_frame = tk.Frame(self, bg='#0a043c')
        button_frame.pack(pady=10)

        button_font = ("Helvetica", 14)
        button_bg = "#61dafb"
        button_fg = "#0a043c"

        self.insert_begin_button = tk.Button(button_frame, text="Insert at Beginning", font=button_font, bg=button_bg, fg=button_fg, command=self.insert_at_beginning, width=18, height=2)
        self.insert_begin_button.pack(side=tk.LEFT, padx=10)

        self.insert_end_button = tk.Button(button_frame, text="Insert at End", font=button_font, bg=button_bg, fg=button_fg, command=self.insert_at_end, width=18, height=2)
        self.insert_end_button.pack(side=tk.LEFT, padx=10)

        self.insert_position_button = tk.Button(button_frame, text="Insert at Position", font=button_font, bg=button_bg, fg=button_fg, command=self.insert_at_position, width=18, height=2)
        self.insert_position_button.pack(side=tk.LEFT, padx=10)

        self.delete_node_button = tk.Button(button_frame, text="Delete Node by Value", font=button_font, bg=button_bg, fg=button_fg, command=self.delete_node, width=18, height=2)
        self.delete_node_button.pack(side=tk.LEFT, padx=10)

        self.delete_position_button = tk.Button(button_frame, text="Delete Node by Index", font=button_font, bg=button_bg, fg=button_fg, command=self.delete_at_position, width=18, height=2)
        self.delete_position_button.pack(side=tk.LEFT, padx=10)

        self.display_button = tk.Button(button_frame, text="Display List", font=button_font, bg=button_bg, fg=button_fg, command=self.display_list, width=18, height=2)
        self.display_button.pack(side=tk.LEFT, padx=10)

        self.quit_button = tk.Button(button_frame, text="Quit", font=button_font, bg=button_bg, fg=button_fg, command=self.quit, width=18, height=2)
        self.quit_button.pack(side=tk.LEFT, padx=10)

        bottom_frame = tk.Frame(self, bg='#0a043c')
        bottom_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Definition frame
        definition_frame = tk.LabelFrame(bottom_frame, text="Definition of Singly Linked List", font=("Helvetica", 14, "bold"), fg="#61dafb", bg='#0a043c', bd=2, padx=10, pady=10)
        definition_frame.pack(side=tk.TOP, fill="both", expand=True, padx=10, pady=10)

        definition_text = ("A singly linked list is a linear data structure where each element (node) points to the next node in the sequence. "
                           "The first node is called the head, and it provides access to the entire list. The last node points to null, indicating the end of the list.")
        definition_label = tk.Label(definition_frame, text=definition_text, font=("Helvetica", 12), fg="#ffffff", bg='#0a043c', wraplength=400, justify="center")
        definition_label.pack(anchor="center")

        # Advantages frame
        advantages_frame = tk.LabelFrame(bottom_frame, text="Advantages of Singly Linked Lists", font=("Helvetica", 14, "bold"), fg="#61dafb", bg='#0a043c', bd=2, padx=10, pady=10)
        advantages_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

        advantages_text = ("1. Dynamic size: Can grow and shrink in size without reallocating memory.\n"
                           "2. Efficient insertions/deletions: Adding or removing nodes does not require shifting elements.\n"
                           "3. Flexibility: Can easily create complex data structures like stacks and queues.\n"
                           "4. Memory usage: Does not require a predefined amount of memory.")
        advantages_label = tk.Label(advantages_frame, text=advantages_text, font=("Helvetica", 12), fg="#ffffff", bg='#0a043c', wraplength=400, justify="left")
        advantages_label.pack(anchor="center")

        # Disadvantages frame
        disadvantages_frame = tk.LabelFrame(bottom_frame, text="Disadvantages of Singly Linked Lists", font=("Helvetica", 14, "bold"), fg="#61dafb", bg='#0a043c', bd=2, padx=10, pady=10)
        disadvantages_frame.pack(side=tk.RIGHT, fill="both", expand=True, padx=10, pady=10)

        disadvantages_text = ("1. Memory overhead: Each node requires additional memory for a pointer.\n"
                              "2. No random access: Must traverse from the head to access elements.\n"
                              "3. Slower access time: Accessing elements is slower compared to arrays.\n"
                              "4. Pointer complexity: Managing pointers can be error-prone and complex.")
        disadvantages_label = tk.Label(disadvantages_frame, text=disadvantages_text, font=("Helvetica", 12), fg="#ffffff", bg='#0a043c', wraplength=400, justify="left")
        disadvantages_label.pack(anchor="center")

        # Key operations frame
        operations_frame = tk.LabelFrame(bottom_frame, text="Key Operations on Singly Linked Lists", font=("Helvetica", 14, "bold"), fg="#61dafb", bg='#0a043c', bd=2, padx=10, pady=10)
        operations_frame.pack(side=tk.BOTTOM, fill="both", expand=True, padx=10, pady=10)

        operations_text = ("1. Insert at Beginning: Adds a node to the start of the list.\n"
                           "2. Insert at End: Adds a node to the end of the list.\n"
                           "3. Insert at Position: Adds a node at a specific position in the list.\n"
                           "4. Delete Node by Value: Removes a node with a specific value from the list.\n"
                           "5. Delete Node by Index: Removes a node at a specific index from the list.\n"
                           "6. Display List: Shows all the nodes present in the list.")
        operations_label = tk.Label(operations_frame, text=operations_text, font=("Helvetica", 12), fg="#ffffff", bg='#0a043c', wraplength=400, justify="left")
        operations_label.pack(anchor="center")

    def update_list_display(self):
        self.list_label.config(text=self.linked_list.display_list())

    def insert_at_beginning(self):
        data = simpledialog.askstring("Input", "Enter data to insert at the beginning:", parent=self)
        if data:
            self.linked_list.insert_at_beginning(data)
            self.update_list_display()
            self.show_info("Insert at Beginning", "Node inserted at the beginning.")
            self.animate_action("insert")

    def insert_at_end(self):
        data = simpledialog.askstring("Input", "Enter data to insert at the end:", parent=self)
        if data:
            self.linked_list.insert_at_end(data)
            self.update_list_display()
            self.show_info("Insert at End", "Node inserted at the end.")
            self.animate_action("insert")

    def insert_at_position(self):
        data = simpledialog.askstring("Input", "Enter data to insert:", parent=self)
        position = simpledialog.askinteger("Input", "Enter position to insert:", parent=self)
        if data and position is not None:
            try:
                self.linked_list.insert_at_position(data, position)
                self.update_list_display()
                self.show_info("Insert at Position", f"Node inserted at position {position}.")
                self.animate_action("insert")
            except IndexError as e:
                self.show_error("Insert at Position Error", str(e))

    def delete_node(self):
        data = simpledialog.askstring("Input", "Enter data of the node to delete:", parent=self)
        if data:
            self.linked_list.delete_node(data)
            self.update_list_display()
            self.show_info("Delete Node by Value", "Node deleted.")
            self.animate_action("delete")

    def delete_at_position(self):
        position = simpledialog.askinteger("Input", "Enter index of the node to delete:", parent=self)
        if position is not None:
            try:
                self.linked_list.delete_at_position(position)
                self.update_list_display()
                self.show_info("Delete Node by Index", f"Node at index {position} deleted.")
                self.animate_action("delete")
            except IndexError as e:
                self.show_error("Delete Node by Index Error", str(e))

    def display_list(self):
        self.update_list_display()
        self.show_info("Display List", self.linked_list.display_list())

    def show_info(self, title, message):
        messagebox.showinfo(title, message, parent=self)

    def show_error(self, title, message):
        messagebox.showerror(title, message, parent=self)

    def animate_action(self, action_type):
        original_color = self.list_label.cget("fg")
        animation_color = "yellow" if action_type == "insert" else "red"
        for _ in range(3):
            self.list_label.config(fg=animation_color)
            self.update()
            self.after(100)
            self.list_label.config(fg=original_color)
            self.update()
            self.after(100)

if __name__ == "__main__":
    app = LinkedListApp()
    app.mainloop()
