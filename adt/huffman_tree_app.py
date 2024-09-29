import heapq
from collections import Counter
from colorama import init
import time
import sys
from tkinter import Tk, Text, Button, Label, Scrollbar, Canvas, Frame, VERTICAL, END, RIGHT, LEFT, Y, BOTH, TOP, W, E

init(autoreset=True)

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies, output_box):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

        output_box.insert(END, f"Merging nodes: {left.char} ({left.freq}) and {right.char} ({right.freq})\n")
        output_box.see(END)
        time.sleep(0.5)

    return heap[0]

def generate_codes(node, prefix="", codebook={}, output_box=None):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
            if output_box:
                output_box.insert(END, f"Assigning code to character {node.char}: {prefix}\n")
                output_box.see(END)
                time.sleep(0.3)
        generate_codes(node.left, prefix + "0", codebook, output_box)
        generate_codes(node.right, prefix + "1", codebook, output_box)
    return codebook

def huffman_encoding(data, output_box):
    if not data:
        return "", {}
 
    frequencies = Counter(data)
    output_box.insert(END, "Character Frequencies: " + str(dict(frequencies)) + "\n")
    output_box.see(END)

    root = build_huffman_tree(frequencies, output_box)
    codebook = generate_codes(root, output_box=output_box)
    encoded_data = ''.join(codebook[char] for char in data)

    output_box.insert(END, "Encoded Data: " + encoded_data + "\n")
    output_box.see(END)
    return encoded_data, codebook, root

def huffman_decoding(encoded_data, codebook, output_box):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_data = ""
    current_code = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data += reverse_codebook[current_code]
            output_box.insert(END, f"Decoding: {current_code} -> {reverse_codebook[current_code]}\n")
            output_box.see(END)
            current_code = ""
            time.sleep(0.2)

    return decoded_data

def animate_text(text, output_box):
    for char in text:
        output_box.insert(END, char)
        output_box.see(END)
        time.sleep(0.05)
    output_box.insert(END, "\n")
    output_box.see(END)

def draw_huffman_tree(node, canvas, x=400, y=50, x_shift=200, y_shift=50):
    if node:
        canvas.create_text(x, y, text=f"{node.char or ''}\n{node.freq}", fill="white")
        if node.left:
            canvas.create_line(x, y, x - x_shift, y + y_shift, fill="white")
            draw_huffman_tree(node.left, canvas, x - x_shift, y + y_shift, x_shift // 2, y_shift)
        if node.right:
            canvas.create_line(x, y, x + x_shift, y + y_shift, fill="white")
            draw_huffman_tree(node.right, canvas, x + x_shift, y + y_shift, x_shift // 2, y_shift)

def start_encoding():
    input_text = input_box.get("1.0", END).strip()
    output_box.delete("1.0", END)
    animate_text("Starting Huffman Encoding...\n", output_box)
    encoded_data, codebook, root = huffman_encoding(input_text, output_box)
    animate_text("Encoding completed!\n", output_box)
    codebook_box.delete("1.0", END)
    codebook_box.insert("1.0", str(codebook))
    encoded_box.delete("1.0", END)
    encoded_box.insert("1.0", encoded_data)
    tree_canvas.delete("all")  # Clear the canvas before drawing the new tree
    draw_huffman_tree(root, tree_canvas)

def start_decoding():
    encoded_data = encoded_box.get("1.0", END).strip()
    codebook = eval(codebook_box.get("1.0", END).strip())
    output_box.delete("1.0", END)
    animate_text("Starting Huffman Decoding...\n", output_box)
    decoded_data = huffman_decoding(encoded_data, codebook, output_box)
    animate_text("Decoding completed!\n", output_box)
    decoded_box.delete("1.0", END)
    decoded_box.insert("1.0", decoded_data)

def exit_application():
    root.quit()

# Create the main window
root = Tk()
root.title("Huffman Coding GUI Application")
root.geometry("900x1000")
root.configure(bg='#2E2E2E')  # Dark grey background

# Create a canvas for scrollable content
canvas = Canvas(root, bg='#2E2E2E')
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add a scrollbar
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame for the content
content_frame = Frame(canvas, bg='#2E2E2E')
canvas.create_window((0, 0), window=content_frame, anchor='nw')

# Update the scroll region of the canvas
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

content_frame.bind("<Configure>", on_frame_configure)

# Labels
Label(content_frame, text="Enter the text to encode:", font=('Arial', 12), bg='#2E2E2E', fg='#F5F5F5').grid(row=0, column=0, sticky="w")
Label(content_frame, text="Abin Pillai S103", font=('Arial', 12), bg='#2E2E2E', fg='#F5F5F5').grid(row=0, column=3, sticky="w")

# Input Text Box
input_box = Text(content_frame, height=5, width=80, font=('Arial', 12), bg='#1E1E1E', fg='#F5F5F5')
input_box.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Buttons
Button(content_frame, text="Encode", command=start_encoding, font=('Arial', 12), bg='#4CAF50', fg='#FFFFFF').grid(row=2, column=0, padx=5, pady=5, sticky="w")
Button(content_frame, text="Decode", command=start_decoding, font=('Arial', 12), bg='#2196F3', fg='#FFFFFF').grid(row=2, column=1, padx=5, pady=5, sticky="w")
Button(content_frame, text="Exit", command=exit_application, font=('Arial', 12), bg='#F44336', fg='#FFFFFF').grid(row=2, column=2, padx=5, pady=5, sticky="e")

# Encoded Data Text Box
Label(content_frame, text="Encoded Data:", font=('Arial', 12), bg='#2E2E2E', fg='#F5F5F5').grid(row=3, column=0, sticky="w")
encoded_box = Text(content_frame, height=5, width=80, font=('Arial', 12), bg='#1E1E1E', fg='#F5F5F5')
encoded_box.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Decoded Data Text Box
Label(content_frame, text="Decoded Data:", font=('Arial', 12), bg='#2E2E2E', fg='#F5F5F5').grid(row=5, column=0, sticky="w")
decoded_box = Text(content_frame, height=5, width=80, font=('Arial', 12), bg='#1E1E1E', fg='#F5F5F5')
decoded_box.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

# Codebook Box
Label(content_frame, text="Codebook:", font=('Arial', 12), bg='#2E2E2E', fg='#F5F5F5').grid(row=7, column=0, sticky="w")
codebook_box = Text(content_frame, height=5, width=80, font=('Arial', 12), bg='#1E1E1E', fg='#F5F5F5')
codebook_box.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

# Output Box for animation and logs
Label(content_frame, text="Output:", font=('Arial', 12), bg='#2E2E2E', fg='#F5F5F5').grid(row=9, column=0, sticky="w")
output_box = Text(content_frame, height=10, width=80, font=('Arial', 12), bg='#1E1E1E', fg='#F5F5F5')
output_box.grid(row=10, column=0, columnspan=3, padx=5, pady=5)

# Canvas for Huffman Tree Visualization
Label(content_frame, text="Huffman Tree Visualization:", font=('Arial', 12), bg='#2E2E2E', fg='#F5F5F5').grid(row=11, column=0, sticky="w")
tree_canvas = Canvas(content_frame, width=800, height=400, bg='#1E1E1E')
tree_canvas.grid(row=12, column=0, columnspan=3, padx=5, pady=5)

# Start the main event loop
root.mainloop()
