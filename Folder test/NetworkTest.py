import networkx as nx
import matplotlib.pyplot as plt

# Buat graf
G = nx.Graph()

# Tambah node
G.add_nodes_from(["A", "B", "C", "D", "E"])

# Tambah edge (hubungan)
G.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E")
])

# Gambar graf
plt.figure(figsize=(10,4))
nx.draw(G, with_labels=True, node_color='skyblue', font_color='black', node_size=1000)
plt.title("Graf Sederhana dengan NetworkX")
plt.margins(0.2)
plt.show()