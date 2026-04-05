import igraph as ig
from igraph import plot

n = 17
step = 3
edges = set()

# For each node, keep every 2nd neighbor in sorted order
for i in range(n):
    neighbors = [i + 1 if i < n - 1 else 0] + [ j for j in range(i + step + 1, n , step)]
    print ("%d: %s" % (i, neighbors))

    for j in neighbors:
        edge = tuple(sorted((i, j)))  # avoid duplicate undirected edges
        edges.add(edge)

# Build graph from the selected edges
g = ig.Graph(n=n, edges=list(edges), directed=False)

# Label nodes
g.vs["label"] = [f"FID {i}" for i in range(n)]

# All shortest paths from 1 to 5, as vertex sequences
paths = g.get_k_shortest_paths(0, to=2, k=3, output="vpath", mode="out")
# paths is a list of lists, e.g. [[1, 3, 5]]



fat_edges = set()
for path in paths:
    # Turn consecutive vertex pairs into edge IDs
    for u, v in zip(path, path[1:]):
        eid = g.get_eid(u, v, directed=False, error=False)
        if eid != -1:
            fat_edges.add(eid)

# Default edge widths
g.es["width"] = [1.0] * g.ecount()
# Make shortest path edges fat
for eid in fat_edges:
    g.es[eid]["width"] = 4.0

# Plot
layout = g.layout_circle()
plot(
    g,
"svg/mesh_%d_every_%dth_neighbor.svg" % (n, step),  # output filename
    layout=layout,
    bbox=(600, 600),
    margin=60,
    vertex_size=30,
    vertex_color="lightblue",
    vertex_label_color="black",
    edge_color="gray"
)