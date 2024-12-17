def bellman_ford(G, w, s):
    d = {}
    pi = {}
    last_v = None

    def initialize_single_source(G, s):
        for v in G:
            d[v] = float("inf")
            pi[v] = None
        d[s] = 0

    def relax(u, v, w):
        if d[v] > d[u] + w[u][v]:
            d[v] = d[u] + w[u][v]
            pi[v] = u

    initialize_single_source(G, s)

    for _ in range(len(G) - 1):
        for u, V in G.items():
            for v in V:
                relax(u, v, w)

    for u, V in G.items():
        for v in V:
            if d[v] > d[u] + w[u][v]:
                raise ValueError(
                    "No path found since there are negative-weight cycles in the graph."
                )

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
    "s": ["t", "y"],
    "t": ["x", "y", "z"],
    "y": ["x", "z"],
    "x": ["t"],
    "z": ["s", "x"],
}
w = {
    "s": {"t": 6, "y": 7},
    "t": {"x": 5, "y": 8, "z": -4},
    "y": {"x": -3, "z": 9},
    "x": {"t": -2},
    "z": {"s": 2, "x": 7},
}
pi, last_v = bellman_ford(G, w, "s")

for v in last_v:
    print_path(G, pi, "s", v)
