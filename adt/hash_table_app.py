import tkinter as tk
from tkinter import messagebox

class HashTable:
    def __init__(self, size):
        """Initialize the hash table with a given size."""
        self.size = size
        self.table = [None] * size  # Use a list of None for each slot

    def hash_function(self, key):
        """Hash function to determine the index for a given key."""
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum % self.size, ascii_sum

    def insert(self, title, author):
        """Insert a book title and author into the hash table."""
        index, ascii_sum = self.hash_function(title)

        if self.table[index] is not None:
            return f"Error: Index {index} is already occupied by '{self.table[index][0]}'."

        self.table[index] = (title, author)
        return f"Inserted book '{title}' by '{author}' at index {index} (ASCII Sum: {ascii_sum})."

    def delete(self, title):
        """Delete the book associated with the given title."""
        index, _ = self.hash_function(title)
        if self.table[index] and self.table[index][0] == title:
            self.table[index] = None
            return f"Deleted book '{title}' from index {index}."
        return f"Book '{title}' not found."

    def search(self, title):
        """Search for the book associated with the given title."""
        index, _ = self.hash_function(title)
        if self.table[index] and self.table[index][0] == title:
            return f"Found book '{title}' by '{self.table[index][1]}' at index {index}."
        return f"Book '{title}' not found."

    def traverse(self):
        """Traverse and return all book entries in the hash table."""
        contents = []
        for index, item in enumerate(self.table):
            if item:
                contents.append(f"Index {index}: Title '{item[0]}', Author '{item[1]}'")
            else:
                contents.append(f"Index {index}: Empty")
        return "\n".join(contents)

class HashTableGUI:
    def __init__(self, root):
        self.hash_table = None
        self.root = root
        self.root.title("Book Library System")
        self.root.geometry("600x600")
        self.root.configure(bg="#2E2E2E")  # Dark background

        # Title Label
        title_label = tk.Label(root, text="Book Library Operations Abin S103", font=("Arial", 20, "bold"), bg="#2E2E2E", fg="yellow")
        title_label.pack(pady=10)

        # Size Input
        size_frame = tk.Frame(root, bg="#2E2E2E")
        size_frame.pack(pady=10)
        size_label = tk.Label(size_frame, text="Enter Size of Hash Table:", font=("Arial", 12), bg="#2E2E2E", fg="white")
        size_label.pack(side=tk.LEFT, padx=5)
        self.size_entry = tk.Entry(size_frame, font=("Arial", 12))
        self.size_entry.pack(side=tk.LEFT, padx=5)

        # Create Button
        create_button = tk.Button(root, text="Create Hash Table", command=self.create_hash_table, font=("Arial", 12), bg="yellow", fg="black")
        create_button.pack(pady=10)

        # Book Title Input
        title_frame = tk.Frame(root, bg="#2E2E2E")
        title_frame.pack(pady=5)
        title_label = tk.Label(title_frame, text="Book Title:", font=("Arial", 12), bg="#2E2E2E", fg="white")
        title_label.pack(side=tk.LEFT, padx=5)
        self.title_entry = tk.Entry(title_frame, font=("Arial", 12), width=30)
        self.title_entry.pack(side=tk.LEFT, padx=5)

        # Author Input
        author_frame = tk.Frame(root, bg="#2E2E2E")
        author_frame.pack(pady=5)
        author_label = tk.Label(author_frame, text="Book Author:", font=("Arial", 12), bg="#2E2E2E", fg="white")
        author_label.pack(side=tk.LEFT, padx=5)
        self.author_entry = tk.Entry(author_frame, font=("Arial", 12), width=30)
        self.author_entry.pack(side=tk.LEFT, padx=5)

        # Buttons Frame
        buttons_frame = tk.Frame(root, bg="#2E2E2E")
        buttons_frame.pack(pady=10)

        insert_button = tk.Button(buttons_frame, text="Insert Book", command=self.insert_book, font=("Arial", 12), bg="yellow", fg="black")
        insert_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(buttons_frame, text="Delete Book", command=self.delete_book, font=("Arial", 12), bg="yellow", fg="black")
        delete_button.pack(side=tk.LEFT, padx=5)

        search_button = tk.Button(buttons_frame, text="Search Book", command=self.search_book, font=("Arial", 12), bg="yellow", fg="black")
        search_button.pack(side=tk.LEFT, padx=5)

        traverse_button = tk.Button(buttons_frame, text="Traverse Library", command=self.traverse_library, font=("Arial", 12), bg="yellow", fg="black")
        traverse_button.pack(side=tk.LEFT, padx=5)

        # Output Text Area
        self.output_text = tk.Text(root, height=10, width=70, font=("Arial", 12), bg="#f0f0f0", fg="black")
        self.output_text.pack(pady=10)

        # Introduction Label
        intro_label = tk.Label(root, text="Introduction:", font=("Arial", 14, "bold"), bg="#2E2E2E", fg="yellow")
        intro_label.pack(pady=5)
        self.intro_text = tk.Text(root, height=5, width=80, font=("Arial", 12), bg="#f0f0f0", fg="black")
        self.intro_text.insert(tk.END, "A Hash Table is a data structure designed to be fast to work with.\n"
                                          "The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching,\n"
                                          "for adding, and deleting data can be done really quickly, even for large amounts of data.\n"
                                          "Handling collisions can be achieved through methods like chaining, where each index points\n"
                                          "to a list of entries, or open addressing, which finds alternative slots in the table.")
        self.intro_text.config(state=tk.DISABLED)  # Make the text box read-only
        self.intro_text.pack(pady=5)

        # Working of Code Label
        working_label = tk.Label(root, text="Working of Code:", font=("Arial", 14, "bold"), bg="#2E2E2E", fg="yellow")
        working_label.pack(pady=5)
        self.working_text = tk.Text(root, height=6, width=80, font=("Arial", 12), bg="#f0f0f0", fg="black")
        self.working_text.insert(tk.END, "This code implements a hash table where each index in the table\n"
                                          "contains a single key-value pair. Users can create a hash table, insert books by title and author,\n"
                                          "delete entries, search for specific books, and traverse the entire table to display contents.\n"
                                          "The hash function computes the index based on the ASCII sum of the book titles, ensuring efficient\n"
                                          "data management with simple collision handling by restricting each index to hold only one entry.\n")
        self.working_text.config(state=tk.DISABLED)  # Make the text box read-only
        self.working_text.pack(pady=5)

    def create_hash_table(self):
        """Create the hash table with the specified size."""
        try:
            size = int(self.size_entry.get())
            self.hash_table = HashTable(size)
            self.output_text.insert(tk.END, f"Hash table of size {size} created.\n")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for size.")

    def insert_book(self):
        """Insert a book into the hash table."""
        if self.hash_table:
            title = self.title_entry.get()
            author = self.author_entry.get()
            result = self.hash_table.insert(title, author)
            if "Error" in result:
                messagebox.showerror("Insertion Error", result)
            else:
                self.output_text.insert(tk.END, result + "\n")
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please create a hash table first.")

    def delete_book(self):
        """Delete a book from the hash table."""
        if self.hash_table:
            title = self.title_entry.get()
            result = self.hash_table.delete(title)
            self.output_text.insert(tk.END, result + "\n")
            self.title_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please create a hash table first.")

    def search_book(self):
        """Search for a book in the hash table."""
        if self.hash_table:
            title = self.title_entry.get()
            result = self.hash_table.search(title)
            self.output_text.insert(tk.END, result + "\n")
            self.title_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please create a hash table first.")

    def traverse_library(self):
        """Traverse the hash table and display all entries."""
        if self.hash_table:
            result = self.hash_table.traverse()
            self.output_text.insert(tk.END, result + "\n")
        else:
            messagebox.showerror("Error", "Please create a hash table first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HashTableGUI(root)
    root.mainloop()
