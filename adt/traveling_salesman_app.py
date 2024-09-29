import tkinter as tk
from tkinter import ttk, messagebox
from itertools import permutations
import math
import matplotlib.pyplot as plt
import networkx as nx

class TSP:
    def __init__(self, distance_matrix, place_names):
        self.distance_matrix = distance_matrix
        self.num_places = len(distance_matrix)
        self.place_names = place_names

    def calculate_total_distance(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i]][route[i + 1]]
        total_distance += self.distance_matrix[route[-1]][route[0]]  # Return to start
        return total_distance

    def solve_brute_force(self):
        min_distance = math.inf
        best_route = None
        for perm in permutations(range(self.num_places)):
            current_distance = self.calculate_total_distance(perm)
            if current_distance < min_distance:
                min_distance = current_distance
                best_route = perm
        return list(best_route) + [best_route[0]], min_distance  # Include return to start

class TSP_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Traveling Salesman Problem - Abin S103")
        self.root.configure(bg='#1a1a40')

        self.place_names = []
        self.distance_matrix = []
        self.entries = {}
        self.predefined_places = ["Dadar Chowpatty", "Mahim Beach", "Juhu Beach", "Versova Beach"]

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Traveling Salesman Problem - Abin S103", font=("Helvetica", 17), bg='#1a1a40', fg='yellow').pack(pady=10)

        tk.Label(self.root, text="Number of Places:", bg='#1a1a40', fg='yellow', font=("Helvetica", 14)).pack()
        self.place_count_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.place_count_entry.pack(pady=5)

        tk.Button(self.root, text="Set Places", command=self.set_places, bg='yellow', fg='#1a1a40', font=("Helvetica", 14)).pack(pady=10)

        self.place_frame = tk.Frame(self.root, bg='#1a1a40')
        self.place_frame.pack()

        self.solve_button = tk.Button(self.root, text="Solve TSP", command=self.solve_brute_force, state='disabled', bg='yellow', fg='#1a1a40', font=("Helvetica", 14))
        self.solve_button.pack(pady=10)

        self.result_textbox = tk.Text(self.root, height=5, width=50, bg='white', fg='black', font=("Helvetica", 14))
        self.result_textbox.pack(pady=10)

    def set_places(self):
        try:
            self.num_places = int(self.place_count_entry.get())
            if self.num_places < 2:
                raise ValueError("Number of places must be at least 2.")

            for widget in self.place_frame.winfo_children():
                widget.destroy()
            self.entries = {}

            tk.Label(self.place_frame, text="Select Place Names:", bg='#1a1a40', fg='yellow', font=("Helvetica", 14)).pack(pady=5)

            self.place_dropdowns = []
            for i in range(self.num_places):
                place_label = tk.Label(self.place_frame, text=f"Place {i + 1}:", bg='#1a1a40', fg='yellow', font=("Helvetica", 14))
                place_label.pack()
                place_dropdown = ttk.Combobox(self.place_frame, values=self.predefined_places, state="readonly", font=("Helvetica", 14))
                place_dropdown.pack()
                self.place_dropdowns.append(place_dropdown)

            tk.Label(self.place_frame, text="Enter Distances (in km):", bg='#1a1a40', fg='yellow', font=("Helvetica", 14)).pack(pady=10)
            self.distance_entries = []

            for i in range(self.num_places):
                row_entries = []
                for j in range(self.num_places):
                    if i == j:
                        row_entries.append(None)  # No self-loops
                    else:
                        entry = tk.Entry(self.place_frame, width=5, font=("Helvetica", 14), validate="key")
                        entry.pack(side='left', padx=2, pady=2)
                        entry.config(validatecommand=(self.root.register(self.validate_numeric), '%P'))
                        row_entries.append(entry)
                self.distance_entries.append(row_entries)

            self.solve_button.config(state='normal')

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))

    def validate_numeric(self, value):
        if value == "":
            return True  # Allow empty input
        try:
            float(value)  # Validate as float
            return True
        except ValueError:
            return False

    def solve_brute_force(self):
        try:
            self.place_names = [dropdown.get() for dropdown in self.place_dropdowns]
            if "" in self.place_names:
                raise ValueError("All place names must be selected.")

            self.distance_matrix = [[0] * self.num_places for _ in range(self.num_places)]
            for i in range(self.num_places):
                for j in range(self.num_places):
                    if i != j:
                        dist = self.distance_entries[i][j].get()
                        if dist == "":
                            raise ValueError("All distances must be filled in.")
                        self.distance_matrix[i][j] = float(dist)

            tsp = TSP(self.distance_matrix, self.place_names)
            best_route, min_distance = tsp.solve_brute_force()

            route_str = " -> ".join(f"{self.place_names[place]}" for place in best_route[:-1])
            self.result_textbox.delete(1.0, tk.END)
            self.result_textbox.insert(tk.END, f"Optimal Route: {route_str}\nTotal Distance: {min_distance:.2f} km")
            print(f"Route using Brute Force: {route_str}, Distance: {min_distance} km")

            self.visualize_route(best_route, self.place_names, self.distance_matrix, "Brute Force", 'blue')

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def visualize_route(self, route, place_names, distance_matrix, method, route_color):
        G = nx.DiGraph()

        for i, place in enumerate(place_names):
            G.add_node(place)

        for i in range(len(route) - 1):
            G.add_edge(place_names[route[i]], place_names[route[i + 1]], weight=distance_matrix[route[i]][route[i + 1]])

        plt.figure(figsize=(10, 10))  # Square format
        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000,
                font_size=10, font_color='black', font_weight='bold', edge_color=route_color, arrows=True)
        
        edge_labels = {(place_names[route[i]], place_names[route[i + 1]]): f"{distance_matrix[route[i]][route[i + 1]]:.1f}" for i in range(len(route) - 1)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

        plt.title(f"TSP Route Visualization ({method})", fontsize=17)
        plt.axis('equal')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = TSP_GUI(root)
    root.mainloop()
