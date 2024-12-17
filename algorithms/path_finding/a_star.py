import heapq


def a_star(G, w, source, goal, heuristic):
    g_score = {}
    f_score = {}
    pi = {}

    for v in G:
        g_score[v] = float("inf")
        f_score[v] = float("inf")
        pi[v] = None
    g_score[source] = 0
    f_score[source] = heuristic(source, goal)

    Q = []
    heapq.heappush(Q, (f_score[source], source))

    while len(Q) > 0:
        _, u = heapq.heappop(Q)
        if u == goal:
            return pi
        for v in G[u]:
            tentative_g_score = g_score[u] + w[u][v]
            if tentative_g_score < g_score[v]:
                pi[v] = u
                g_score[v] = tentative_g_score
                f_score[v] = tentative_g_score + heuristic(v, goal)
                if v not in Q:
                    heapq.heappush(Q, (f_score[v], v))

    raise ValueError("Goal was never reached.")


def heuristic(current, goal):
    d = (current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2
    return d


def print_path(G, pi, s, v):
    if v == s:
        print(s)
    elif not pi.get(v):
        print(f"No path from {s} to {v} exists")
    else:
        print_path(G, pi, s, pi[v])
        print(v)


G = {
    (0, 9): [(7, 1), (5, 0), (3, 0)],
    (1, 0): [(2, 4), (7, 1)],
    (7, 7): [(8, 0), (3, 0)],
    (7, 1): [(3, 0)],
    (5, 0): [(8, 7)],
    (3, 0): [(8, 0), (8, 7), (2, 4)],
    (8, 7): [],
    (8, 0): [],
    (2, 4): [],
}
w = {
    (0, 9): {(7, 1): 10.5, (5, 0): 15.2, (3, 0): 3.7},
    (1, 0): {(2, 4): 17.1, (7, 1): 13.3},
    (7, 7): {(8, 0): 13.6, (3, 0): 20.4},
    (7, 1): {(3, 0): 15.8},
    (5, 0): {(8, 7): 17.5},
    (3, 0): {(8, 0): 14.3, (8, 7): 7.8, (2, 4): 15.9},
    (8, 7): {},
    (8, 0): {},
    (2, 4): {},
}
pi = a_star(G, w, (1, 0), (8, 0), heuristic)
print_path(G, pi, (1, 0), (8, 0))
