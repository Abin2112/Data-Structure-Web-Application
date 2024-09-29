from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Main page with buttons
    path('run_stack/', views.run_stack, name='run_stack'),
    path('run_singly_linked_list/', views.run_singly_linked_list, name='run_singly_linked_list'),
    path('run_doubly_linked_list/', views.run_doubly_linked_list, name='run_doubly_linked_list'),
    path('run_queue/', views.run_queue, name='run_queue'),
    path('run_priority_queue/', views.run_priority_queue, name='run_priority_queue'),
    path('run_priority_queue_heapq/', views.run_priority_queue_heapq, name='run_priority_queue_heapq'),
    path('run_binary_tree/', views.run_binary_tree, name='run_binary_tree'),
    path('run_huffman_tree/', views.run_huffman_tree, name='run_huffman_tree'),
    path('run_graph/', views.run_graph, name='run_graph'),
    path('run_graph_bfs_dfs/', views.run_graph_bfs_dfs, name='run_graph_bfs_dfs'),
    path('run_traveling_salesman/', views.run_traveling_salesman, name='run_traveling_salesman'),
    path('run_hash_table/', views.run_hash_table, name='run_hash_table'),
    path('run_hash_table_collision/', views.run_hash_table_collision, name='run_hash_table_collision'),
]
