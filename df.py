import igraph as ig
from igraph import plot

n = 17
step = 3
edges = set()

print (ig.__version__)

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
g.vs["name"] = [f"{i}" for i in range(n)]
g.vs["label"] = [f"{i}" for i in range(n)]

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

# remove fid 0 and show fid 13 all shortest to 2

gno0 = g.copy()

gno0.delete_vertices("0")
gno0.delete_vertices("12")

print([gno["name"] for gno in gno0.vs])

from13to2 = gno0.get_all_shortest_paths("13", to="2")

print (from13to2)

dashed_edges = set()
for path in from13to2:
    # Turn consecutive vertex pairs into edge IDs
    for u, v in zip(path, path[1:]):
        eid = g.get_eid(gno0.vs[u]["name"], gno0.vs[v]["name"], directed=False, error=False)
        if eid != -1:
            dashed_edges.add(eid)
            pass
        pass
    pass

styles = []
for eid in range(g.ecount()):
    if eid in dashed_edges:
        g.es[eid]["width"] = 3.0
        styles.append("dashed")
        pass
    elif eid in fat_edges:
        g.es[eid]["width"] = 6.0
        styles.append("solid")
        pass
    else:
        styles.append("solid")
    pass

print (styles)

# Plot
layout = g.layout_circle()
plot(
    g,
"svg/mesh_%d_every_%dth_neighbor.svg" % (n, step),  # output filename
    layout=layout,
    # bbox=(600, 600),
    # margin=60,
    # vertex_size=30,
    vertex_color="white",
    vertex_label_color="black",
    edge_color="black",
    edge_label_color="black",
    edge_style = styles,
)