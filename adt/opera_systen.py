import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graph Operations")
        self.geometry("1200x800")
        self.configure(bg='#0a043c')

        # Initialize Graph
        self.graph = nx.Graph()
        self.edge_colors = {}  # To store edge colors

        # Create Widgets
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(
            self,
            text="Graph Operations - Abin S103",
            font=("Helvetica", 24, "bold"),
            fg="#f3ffbd",
            bg='#0a043c'
        )
        self.title_label.pack(pady=20)
    
        # Canvas for Graph Plot
        self.figure = plt.figure(figsize=(6, 6), facecolor='#0a043c')
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Control Frame
        control_frame = tk.Frame(self, bg='#0a043c')
        control_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        button_font = ("Helvetica", 14)
        button_bg = "#61dafb"
        button_fg = "#0a043c"
        button_width = 20
        button_height = 2

        # Add Vertex Button
        self.add_vertex_button = tk.Button(
            control_frame,
            text="Add Vertex",
            font=button_font,
            bg=button_bg,
            fg=button_fg,
            width=button_width,
            height=button_height,
            command=self.add_vertex
        )
        self.add_vertex_button.grid(row=0, column=0, padx=5, pady=5)

        # Remove Vertex Button
        self.remove_vertex_button = tk.Button(
            control_frame,
            text="Remove Vertex",
            font=button_font,
            bg=button_bg,
            fg=button_fg,
            width=button_width,
            height=button_height,
            command=self.remove_vertex
        )
        self.remove_vertex_button.grid(row=0, column=1, padx=5, pady=5)

        # Add Edge Button
        self.add_edge_button = tk.Button(
            control_frame,
            text="Add Edge",
            font=button_font,
            bg=button_bg,
            fg=button_fg,
            width=button_width,
            height=button_height,
            command=self.add_edge
        )
        self.add_edge_button.grid(row=1, column=0, padx=5, pady=5)

        # Remove Edge Button
        self.remove_edge_button = tk.Button(
            control_frame,
            text="Remove Edge",
            font=button_font,
            bg=button_bg,
            fg=button_fg,
            width=button_width,
            height=button_height,
            command=self.remove_edge
        )
        self.remove_edge_button.grid(row=1, column=1, padx=5, pady=5)

        # Clear Graph Button
        self.clear_graph_button = tk.Button(
            control_frame,
            text="Clear Graph",
            font=button_font,
            bg="#ff6b6b",
            fg="#ffffff",
            width=button_width,
            height=button_height,
            command=self.clear_graph
        )
        self.clear_graph_button.grid(row=2, column=0, padx=5, pady=5)

        # Quit Button
        self.quit_button = tk.Button(
            control_frame,
            text="Quit",
            font=button_font,
            bg="#f3ffbd",
            fg="#0a043c",
            width=button_width,
            height=button_height,
            command=self.quit
        )
        self.quit_button.grid(row=2, column=1, padx=5, pady=5)

        # Instructions and Operations Information
        instruction_text = (
            "Instructions:\n\n"
            "1. Use the buttons to modify the graph.\n"
            "2. The graph visualization updates automatically.\n"
            "3. You can add vertices and edges as needed.\n"
            "4. Remove vertices or edges using their identifiers.\n"
            "5. Clear the entire graph using the 'Clear Graph' button."
        )
        self.instruction_label = tk.Label(
            control_frame,
            text=instruction_text,
            font=("Helvetica", 14),
            fg="#f3ffbd",
            bg='#0a043c',
            justify="left",
            wraplength=600
        )
        self.instruction_label.grid(row=3, column=0, columnspan=2, pady=20)

        # Initial Graph Drawing
        self.draw_graph()

    def draw_graph(self):
        plt.clf()
        pos = nx.spring_layout(self.graph)  # Recalculate layout
        edge_colors = [self.edge_colors.get(edge, '#f3ffbd') for edge in self.graph.edges]
        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_color='#61dafb',
            edge_color=edge_colors,
            font_size=12,
            font_weight='bold',
            node_size=800
        )
        self.canvas.draw()

    def add_vertex(self):
        vertex = simpledialog.askstring("Add Vertex", "Enter vertex label:", parent=self)
        if vertex:
            vertex = vertex.strip()
            if vertex in self.graph.nodes:
                messagebox.showerror("Error", f"Vertex '{vertex}' already exists.")
            else:
                self.graph.add_node(vertex)
                self.draw_graph()
                messagebox.showinfo("Success", f"Vertex '{vertex}' added successfully.")

    def remove_vertex(self):
        vertex = simpledialog.askstring("Remove Vertex", "Enter vertex label to remove:", parent=self)
        if vertex:
            vertex = vertex.strip()
            if vertex in self.graph.nodes:
                self.graph.remove_node(vertex)
                self.draw_graph()
                messagebox.showinfo("Success", f"Vertex '{vertex}' removed successfully.")
            else:
                messagebox.showerror("Error", f"Vertex '{vertex}' does not exist.")

    def add_edge(self):
        edge_dialog = EdgeDialog(self, "Add Edge")
        self.wait_window(edge_dialog.top)
        if edge_dialog.result != (None, None):
            u, v = edge_dialog.result
            u, v = u.strip(), v.strip()
            if u and v:
                if u not in self.graph.nodes or v not in self.graph.nodes:
                    messagebox.showerror("Error", f"Both vertices '{u}' and '{v}' must exist to add an edge.")
                elif self.graph.has_edge(u, v):
                    messagebox.showerror("Error", f"Edge '{u}-{v}' already exists.")
                else:
                    self.graph.add_edge(u, v)
                    self.edge_colors[(u, v)] = '#000000'  # Set edge color to black
                    self.draw_graph()
                    messagebox.showinfo("Success", f"Edge '{u}-{v}' added successfully.")

    def remove_edge(self):
        edge_dialog = EdgeDialog(self, "Remove Edge")
        self.wait_window(edge_dialog.top)
        if edge_dialog.result != (None, None):
            u, v = edge_dialog.result
            u, v = u.strip(), v.strip()
            if u and v:
                if not self.graph.has_edge(u, v):
                    messagebox.showerror("Error", f"Edge '{u}-{v}' does not exist.")
                else:
                    self.graph.remove_edge(u, v)
                    self.draw_graph()
                    messagebox.showinfo("Success", f"Edge '{u}-{v}' removed successfully.")

    def clear_graph(self):
        self.graph.clear()
        self.draw_graph()
        messagebox.showinfo("Success", "Graph cleared successfully.")

class EdgeDialog:
    def __init__(self, parent, title):
        self.top = tk.Toplevel(parent)
        self.top.title(title)
        self.parent = parent

        tk.Label(self.top, text="Enter the two vertices (separated by a comma):").pack(pady=10)

        self.entry = tk.Entry(self.top, width=40)
        self.entry.pack(pady=10)

        tk.Button(self.top, text="OK", command=self.ok).pack(side=tk.LEFT, padx=10)
        tk.Button(self.top, text="Cancel", command=self.cancel).pack(side=tk.RIGHT, padx=10)

        self.result = (None, None)

    def ok(self):
        entry_text = self.entry.get()
        vertices = entry_text.split(',')
        if len(vertices) == 2:
            self.result = (vertices[0].strip(), vertices[1].strip())
        self.top.destroy()

    def cancel(self):
        self.top.destroy()

if __name__ == "__main__":
    app = GraphGUI()
    app.mainloop()
