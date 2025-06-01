import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Membuat graf kosong
Graph = nx.Graph()

# Daftar node dan nama lokasinya
nodes = {
    'A': 'Gerbang Depan',
    'B': 'FEB',
    'C': 'FC',
    'D': 'Danau Unesa',
    'E': 'Vokasi',
    'F': 'Masjid Unesa',
    'G': 'FMIPA',
    'H': 'FISH',
    'I': 'FT',
    'J': 'Gerbang Belakang'
}

# Menambahkan simpul ke graf
Graph.add_nodes_from(nodes.keys())

# Menambahkan edge utama dan alternatif (jalur tidak hanya satu)
Graph.add_edge('A', 'B', weight=1)
Graph.add_edge('A', 'C', weight=1)
Graph.add_edge('B', 'D', weight=1)
Graph.add_edge('C', 'D', weight=1)
Graph.add_edge('C', 'E', weight=1)      
Graph.add_edge('D', 'F', weight=1)      
Graph.add_edge('E', 'F', weight=1)
Graph.add_edge('F', 'G', weight=1)
Graph.add_edge('G', 'H', weight=1)
Graph.add_edge('G', 'I', weight=1)     
Graph.add_edge('H', 'I', weight=1)
Graph.add_edge('I', 'J', weight=1)

# Fungsi untuk menampilkan daftar lokasi
def show_routes():
    print("\n📍 Daftar Titik Lokasi:")
    for kode, nama in nodes.items():
        print(f"{kode} : {nama}")

# Fungsi BFS untuk mencari jalur dari start ke goal
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

# Fungsi untuk menampilkan graf dan rute BFS
def show_graph(route=None):
    pos = nx.spring_layout(Graph, seed=42)
    nx.draw(Graph, pos, with_labels=False, node_color='lightblue', node_size=2000)

    label_pos = {k: (v[0], v[1] + 0.05) for k, v in pos.items()}
    nx.draw_networkx_labels(Graph, label_pos, labels=nodes, font_size=10)

    if route:
        highlighted_edges = [(route[i], route[i+1]) for i in range(len(route)-1)]
        nx.draw_networkx_edges(Graph, pos, edgelist=highlighted_edges, edge_color='red', width=2)

    plt.title("Graf Lokasi & Jalur BFS")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Menu utama
while True:
    print("\n📌 MENU UTAMA")
    print("1. Tampilkan Daftar Titik")
    print("2. Cari Jalur BFS dan Tampilkan Graf")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ").strip()

    if pilihan == '1':
        show_routes()

    elif pilihan == '2':
        show_routes()
        start = input("Masukkan titik awal (contoh: A): ").strip().upper()
        goal = input("Masukkan titik tujuan (contoh: J): ").strip().upper()

        if start in Graph.nodes and goal in Graph.nodes:
            path = bfs(Graph, start, goal)
            if path:
                print(f"\n🧭 Jalur BFS dari {start} ke {goal}: {' -> '.join(path)}")
                print("📍 Rute Tempat:")
                for p in path:
                    print(f"{p} : {nodes[p]}")
                show_graph(path)
            else:
                print("⚠️ Jalur tidak ditemukan.")
        else:
            print("⚠️ Titik tidak valid. Silakan coba lagi.")

    elif pilihan == '3':
        print("👋 Keluar dari program.")
        break
    else:
        print("⚠️ Pilihan tidak valid. Coba lagi.")
