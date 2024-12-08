def dag_shortest_paths(G, w, s):
    d = {}
    pi = {}

    def topological_sort(G):
        visited = {}
        vertices = []

        def visit(G, u):
            visited[u] = True
            for v in G[u]:
                if not visited.get(v, False):
                    visit(G, v)
            vertices.append(u)

        for u in G:
            if not visited.get(u, False):
                visit(G, u)

        vertices = vertices[::-1]

        return vertices

    def initialize_single_source(G, s):
        for v in G:
            d[v] = float("inf")
            pi[v] = None
        d[s] = 0

    def relax(u, v, w):
        if d[v] > d[u] + w[u][v]:
            d[v] = d[u] + w[u][v]
            pi[v] = u

    vertices = topological_sort(G)
    initialize_single_source(G, s)
    for u in vertices:
        for v in G[u]:
            relax(u, v, w)

    last_v = []
    for v in G.keys():
        if v not in pi.values() and pi[v] is not None:
            last_v.append(v)

    return pi, last_v


def print_path(G, pi, s, v):
    if v == s:
        print(s)
    elif not pi.get(v):
        print(f"No path from {s} to {v} exists")
    else:
        print_path(G, pi, s, pi[v])
        print(v)


G = {
    "s": ["t", "x"],
    "t": ["x", "y", "z"],
    "y": ["z"],
    "z": [],
    "x": ["y", "z"],
    "r": ["s", "t"],
}
w = {
    "s": {"t": 2, "x": 6},
    "t": {"x": 7, "y": 4, "z": 2},
    "y": {"z": -2},
    "z": {},
    "x": {"y": -1, "z": 1},
    "r": {"s": 5, "t": 3},
}
pi, last_v = dag_shortest_paths(G, w, "s")

for v in last_v:
    print_path(G, pi, "s", v)
