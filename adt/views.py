from django.shortcuts import render
from django.http import HttpResponse
import subprocess  # To run your apps

# View to display the main page with buttons
def home(request):
    return render(request, 'adt/index.html')

# View to run Stack operations
def run_stack(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/stack_app.py'])
        return HttpResponse("<h1>Stack Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Singly Linked List operations
def run_singly_linked_list(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/singly_linked_list_app.py'])
        return HttpResponse("<h1>Singly Linked List Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Doubly Linked List operations
def run_doubly_linked_list(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/doubly_linked_list_app.py'])
        return HttpResponse("<h1>Doubly Linked List Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Queue operations
def run_queue(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/queue_app.py'])
        return HttpResponse("<h1>Queue Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Priority Queue operations without heapq
def run_priority_queue(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/priority_queue_app.py'])
        return HttpResponse("<h1>Priority Queue (without heapq) Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Priority Queue operations using heapq
def run_priority_queue_heapq(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/priority_queue_heapq_app.py'])
        return HttpResponse("<h1>Priority Queue (with heapq) Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Binary Tree operations
def run_binary_tree(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/binary_tree_app.py'])
        return HttpResponse("<h1>Binary Tree Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Huffman Coding using Tree
def run_huffman_tree(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/huffman_tree_app.py'])
        return HttpResponse("<h1>Huffman Tree Coding Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Graph operations
def run_graph(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/opera_systen.py'])
        return HttpResponse("<h1>Graph Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Graph BFS & DFS operations
def run_graph_bfs_dfs(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/graph_bfs_dfs_app.py'])
        return HttpResponse("<h1>Graph BFS & DFS Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Traveling Salesman Problem operations
def run_traveling_salesman(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/traveling_salesman_app.py'])
        return HttpResponse("<h1>Traveling Salesman Problem Operations are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Hash Table operations without collisions
def run_hash_table(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/hash_table_app.py'])
        return HttpResponse("<h1>Hash Table Operations (No Collisions) are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# View to run Hash Table operations with collisions
def run_hash_table_collision(request):
    if request.method == "POST":
        subprocess.Popen(['python', 'adt/hash_table_collision_app.py'])
        return HttpResponse("<h1>Hash Table Operations (With Collisions) are running. Check your system!</h1>")
    return HttpResponse("<h1>Invalid request</h1>")
