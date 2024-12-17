import heapq


def dijkstra(G, w, s):
    d = {}
    pi = {}

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

    S = []
    Q = []

    for u in G:
        heapq.heappush(Q, (d[u], u))

    while len(Q) > 0:
        _, u = heapq.heappop(Q)
        S.append(u)
        for v in G[u]:
            old_d = d[v]
            relax(u, v, w)
            if d[v] < old_d:
                heapq.heappush(Q, (d[v], v))

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
    "t": ["x", "y"],
    "x": ["z"],
    "y": ["t", "x", "z"],
    "z": ["s", "x"],
}
w = {
    "s": {"t": 10, "y": 5},
    "t": {"x": 1, "y": 2},
    "x": {"z": 4},
    "y": {"t": 3, "x": 9, "z": 2},
    "z": {"s": 7, "x": 6},
}
pi, last_v = dijkstra(G, w, "s")

for v in last_v:
    print_path(G, pi, "s", v)
