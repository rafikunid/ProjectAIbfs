import tkinter as tk
from tkinter import messagebox, ttk
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Buat graf kosong
Graph = nx.Graph()

# Nama-nama node
nodes = {
    'A': 'Gerbang Depan',
    'B': 'Masjid unesa',
    'C': 'Vokasi',
    'D': 'FC',
    'E': 'Danau unesa',
    'F': 'FMIPA',
    'G': 'FEB',
    'H': 'FISH',
    'I': 'FT',
    'J': 'Gerbang Belakang'
}

Graph.add_nodes_from(nodes.keys())

edges = [
    ('A', 'C'), ('A', 'D'), ('A', 'B'), ('B', 'A'), ('B', 'D'), ('B', 'F'), ('B', 'J'),
    ('C', 'A'), ('C', 'D'), ('C', 'G'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'E'), ('D', 'F'),
    ('E', 'C'), ('E', 'D'), ('E', 'F'), ('E', 'I'), ('E', 'H'), ('E', 'G'),
    ('F', 'B'), ('F', 'D'), ('F', 'E'), ('F', 'I'), ('F', 'J'),
    ('G', 'C'), ('G', 'E'), ('G', 'H'), ('H', 'G'), ('H', 'E'), ('H', 'I'),
    ('I', 'H'), ('I', 'E'), ('I', 'F'), ('I', 'J'),
    ('J', 'B'), ('J', 'F'), ('J', 'I')
]

for u, v in edges:
    Graph.add_edge(u, v, weight=5)

# Fungsi BFS
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in path:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
    return None

# Tampilkan graf dengan rute
def show_graph(route=None):
    pos = nx.spring_layout(Graph, seed=42)
    nx.draw(Graph, pos, with_labels=False, node_color='lightblue', node_size=2000)

    label_pos = {k: (v[0], v[1] + 0.05) for k, v in pos.items()}
    nx.draw_networkx_labels(Graph, label_pos, labels=nodes, font_size=10)

    if route:
        highlighted_edges = [(route[i], route[i + 1]) for i in range(len(route) - 1)]
        nx.draw_networkx_edges(Graph, pos, edgelist=highlighted_edges, edge_color='red', width=2)

    plt.title("Graf Lokasi Kampus")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# GUI
def run_gui():
    root = tk.Tk()
    root.title("Pencarian Jalur BFS Lokasi Unesa")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    tk.Label(frame, text="Titik Awal:").grid(row=0, column=0, sticky='w')
    start_var = tk.StringVar()
    start_menu = ttk.Combobox(frame, textvariable=start_var, values=list(nodes.keys()))
    start_menu.grid(row=0, column=1)

    tk.Label(frame, text="Titik Tujuan:").grid(row=1, column=0, sticky='w')
    goal_var = tk.StringVar()
    goal_menu = ttk.Combobox(frame, textvariable=goal_var, values=list(nodes.keys()))
    goal_menu.grid(row=1, column=1)

    result_text = tk.Text(frame, height=10, width=50)
    result_text.grid(row=3, column=0, columnspan=2, pady=10)

    def cari_jalur():
        start = start_var.get().upper()
        goal = goal_var.get().upper()

        if start not in Graph.nodes or goal not in Graph.nodes:
            messagebox.showerror("Error", "Titik tidak valid.")
            return

        path = bfs(Graph, start, goal)
        if path:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Jalur BFS dari {start} ke {goal}:\n")
            result_text.insert(tk.END, ' -> '.join(path) + '\n\n')
            result_text.insert(tk.END, "Rute Tempat:\n")
            for p in path:
                result_text.insert(tk.END, f"{p} : {nodes[p]}\n")
            show_graph(path)
        else:
            messagebox.showinfo("Hasil", "Jalur tidak ditemukan.")

    btn_cari = tk.Button(frame, text="Cari Jalur & Tampilkan Graf", command=cari_jalur)
    btn_cari.grid(row=2, column=0, columnspan=2, pady=5)

    root.mainloop()

run_gui()
