import tkinter as tk
from tkinter import messagebox, ttk
import time
from threading import Thread
import heapq

class PriorityQueue:
    def __init__(self, max_size):
        self.queue = []
        self.heap_queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.max_size

    def enqueue(self, item, priority):
        if self.is_full():
            return False
        else:
            self.queue.append((priority, item))
            heapq.heappush(self.heap_queue, (priority, item))
            return True

    def dequeue(self):
        if self.is_empty():
            return None
        priority, item = heapq.heappop(self.heap_queue)
        self.queue.remove((priority, item))
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.heap_queue[0][1]

    def traverse(self):
        return sorted(self.queue, key=lambda x: x[0])

    def traverse_descending(self):
        return sorted(self.queue, key=lambda x: x[0], reverse=True)

class PriorityQueueGUI:
    def __init__(self, root, max_size):
        self.queue = PriorityQueue(max_size)
        self.root = root
        self.root.title("Priority Queue Operations")
        self.root.geometry("900x600")
        self.root.configure(bg="darkblue")
        self.max_size = max_size

        self.create_widgets()
        self.update_progress_bar()

    def create_widgets(self):
        # Queue Display
        self.queue_frame = tk.Frame(self.root, bg="darkblue")
        self.queue_frame.pack(pady=10)
        self.queue_display = tk.Label(self.queue_frame, text="Queue: []", font=("Helvetica", 14), bg="darkblue", fg="yellow")
        self.queue_display.pack()

        # Controls
        self.controls_frame = tk.Frame(self.root, bg="darkblue")
        self.controls_frame.pack(pady=10)

        self.entry_label = tk.Label(self.controls_frame, text="Enter Item:", font=("Helvetica", 14), bg="darkblue", fg="yellow")
        self.entry_label.pack(side=tk.LEFT, padx=5)
        self.entry = tk.Entry(self.controls_frame, font=("Helvetica", 10))
        self.entry.pack(side=tk.LEFT, padx=5)

        self.priority_label = tk.Label(self.controls_frame, text="Enter Priority:", font=("Helvetica", 14), bg="darkblue", fg="yellow")
        self.priority_label.pack(side=tk.LEFT, padx=5)
        self.priority_entry = tk.Entry(self.controls_frame, font=("Helvetica", 10))
        self.priority_entry.pack(side=tk.LEFT, padx=5)

        self.enqueue_button = tk.Button(self.controls_frame, text="Enqueue", command=self.enqueue, font=("Helvetica", 14), bg="yellow", fg="darkblue")
        self.enqueue_button.pack(side=tk.LEFT, padx=5)

        self.dequeue_button = tk.Button(self.controls_frame, text="Dequeue", command=self.dequeue, font=("Helvetica", 14), bg="yellow", fg="darkblue")
        self.dequeue_button.pack(side=tk.LEFT, padx=5)

        self.peek_button = tk.Button(self.controls_frame, text="Peek", command=self.peek, font=("Helvetica", 14), bg="yellow", fg="darkblue")
        self.peek_button.pack(side=tk.LEFT, padx=5)

        self.empty_button = tk.Button(self.controls_frame, text="Is Empty?", command=self.is_empty, font=("Helvetica", 14), bg="yellow", fg="darkblue")
        self.empty_button.pack(side=tk.LEFT, padx=5)

        self.full_button = tk.Button(self.controls_frame, text="Is Full?", command=self.is_full, font=("Helvetica", 14), bg="yellow", fg="darkblue")
        self.full_button.pack(side=tk.LEFT, padx=5)

        self.traverse_button = tk.Button(self.controls_frame, text="Traverse Ascending", command=self.traverse, font=("Helvetica", 14), bg="yellow", fg="darkblue")
        self.traverse_button.pack(side=tk.LEFT, padx=5)

        self.traverse_desc_button = tk.Button(self.controls_frame, text="Traverse Descending", command=self.traverse_descending, font=("Helvetica", 14), bg="yellow", fg="darkblue")
        self.traverse_desc_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(self.controls_frame, text="Exit", command=self.root.quit, font=("Helvetica", 14), bg="red", fg="white")
        self.exit_button.pack(side=tk.LEFT, padx=5)

        # Progress Bar
        self.progress_frame = tk.Frame(self.root, bg="darkblue")
        self.progress_frame.pack(pady=10)
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack()

        # History Log
        self.log_frame = tk.Frame(self.root, bg="darkblue")
        self.log_frame.pack(pady=10)
        self.log_label = tk.Label(self.log_frame, text="History Log", font=("Helvetica", 14), bg="darkblue", fg="yellow")
        self.log_label.pack()
        self.log_text = tk.Text(self.log_frame, width=60, height=10, font=("Helvetica", 12), bg="black", fg="white")
        self.log_text.pack()

        # Theme Customization
        self.theme_frame = tk.Frame(self.root, bg="darkblue")
        self.theme_frame.pack(pady=10)
        self.theme_label = tk.Label(self.theme_frame, text="Theme:", font=("Helvetica", 14), bg="darkblue", fg="yellow")
        self.theme_label.pack(side=tk.LEFT, padx=5)
        self.theme_var = tk.StringVar(value="darkblue")
        self.theme_menu = ttk.Combobox(self.theme_frame, textvariable=self.theme_var, values=["darkblue", "black", "gray", "Maroon", "purple", "Forest Green", "Dark Red", "Dark Green"])
        self.theme_menu.pack(side=tk.LEFT, padx=5)
        self.theme_menu.bind("<<ComboboxSelected>>", self.change_theme)

        # Queue Definition
        self.definition_frame = tk.Frame(self.root, bg="darkblue")
        self.definition_frame.pack(pady=10, fill=tk.X)
        self.definition_label = tk.Label(self.definition_frame, text="About The Program:", font=("Helvetica", 20), bg="darkblue", fg="yellow")
        self.definition_label.pack()
        self.definition_text = tk.Text(self.definition_frame, width=90, height=10, font=("Helvetica", 16), bg="darkblue", fg="yellow", wrap=tk.WORD)
        self.definition_text.insert(tk.END, "A priority queue is a type of queue where each element is associated with a priority and elements are dequeued in priority order. "
                                           "The operations performed on a priority queue include:\n"
                                           "1. Enqueue: Add an item with its priority to the queue.\n"
                                           "2. Dequeue: Remove the item with the highest priority.\n"
                                           "3. Peek: View the item with the highest priority without removing it.\n"
                                           "4. Is Empty: Check if the queue is empty.\n"
                                           "5. Is Full: Check if the queue is full.")
        self.definition_text.config(state=tk.DISABLED)
        self.definition_text.pack()

    def change_theme(self, event):
        selected_theme = self.theme_var.get()
        self.root.configure(bg=selected_theme)
        self.queue_frame.configure(bg=selected_theme)
        self.controls_frame.configure(bg=selected_theme)
        self.progress_frame.configure(bg=selected_theme)
        self.log_frame.configure(bg=selected_theme)
        self.theme_frame.configure(bg=selected_theme)
        self.queue_display.configure(bg=selected_theme)
        self.log_label.configure(bg=selected_theme)
        self.log_text.configure(bg=selected_theme)
        self.theme_label.configure(bg=selected_theme)
        self.definition_frame.configure(bg=selected_theme)
        self.definition_label.configure(bg=selected_theme)
        self.definition_text.configure(bg=selected_theme)

    def log_operation(self, operation):
        self.log_text.insert(tk.END, operation + "\n")
        self.log_text.see(tk.END)

    def play_sound(self, sound):
        sound.play()

    def update_display(self):
        self.queue_display.config(text=f"Queue: {[(item[1], item[0]) for item in self.queue.traverse()]}")
        self.queue_display.update()

    def update_progress_bar(self):
        self.progress_bar["value"] = (len(self.queue.queue) / self.queue.max_size) * 100
        self.progress_bar.update()

    def animate_enqueue(self, item):
        for _ in range(3):
            self.queue_display.config(fg="red")
            self.queue_display.update()
            time.sleep(0.1)
            self.queue_display.config(fg="yellow")
            self.queue_display.update()
            time.sleep(0.1)

    def animate_dequeue(self):
        for _ in range(3):
            self.queue_display.config(fg="green")
            self.queue_display.update()
            time.sleep(0.1)
            self.queue_display.config(fg="yellow")
            self.queue_display.update()
            time.sleep(0.1)

    def enqueue(self):
        item = self.entry.get()
        try:
            priority = int(self.priority_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Priority must be an integer")
            return

        if not item:
            messagebox.showerror("Invalid input", "Item cannot be empty")
            return

        if self.queue.enqueue(item, priority):
            self.update_display()
            self.update_progress_bar()
            self.log_operation(f"Enqueued: {item} with priority {priority}")
            self.play_sound(self.enqueue_sound)
            Thread(target=self.animate_enqueue, args=(item,)).start()
        else:
            messagebox.showwarning("Queue Full", "Cannot enqueue, the queue is full")

    def dequeue(self):
        item = self.queue.dequeue()
        if item:
            self.update_display()
            self.update_progress_bar()
            self.log_operation(f"Dequeued: {item}")
            self.play_sound(self.dequeue_sound)
            Thread(target=self.animate_dequeue).start()
        else:
            messagebox.showwarning("Queue Empty", "Cannot dequeue, the queue is empty")

    def peek(self):
        item = self.queue.peek()
        if item:
            messagebox.showinfo("Peek", f"The item with the highest priority is: {item}")
        else:
            messagebox.showwarning("Queue Empty", "The queue is empty")

    def is_empty(self):
        if self.queue.is_empty():
            messagebox.showinfo("Is Empty?", "Yes, the queue is empty")
        else:
            messagebox.showinfo("Is Empty?", "No, the queue is not empty")

    def is_full(self):
        if self.queue.is_full():
            messagebox.showinfo("Is Full?", "Yes, the queue is full")
        else:
            messagebox.showinfo("Is Full?", "No, the queue is not full")

    def traverse(self):
        items = self.queue.traverse()
        traverse_items = [(item[1], item[0]) for item in items]
        messagebox.showinfo("Traverse Ascending", f"Queue items (ascending order): {traverse_items}")

    def traverse_descending(self):
        items = self.queue.traverse_descending()
        traverse_items = [(item[1], item[0]) for item in items]
        messagebox.showinfo("Traverse Descending", f"Queue items (descending order): {traverse_items}")

if __name__ == "__main__":
    root = tk.Tk()
    max_size = 10
    app = PriorityQueueGUI(root, max_size)
    root.mainloop()
