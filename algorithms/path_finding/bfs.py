def BFS(G, s):
    visited = {}
    visited[s] = True
    Q = []
    Q.append(s)
    while len(Q) > 0:
        u = Q.pop(0)
        print(u)
        for v in G[u]:
            if not visited.get(v, False):
                visited[v] = True
                Q.append(v)


G = {1: [2, 4], 2: [5], 3: [6, 5], 4: [2], 5: [4], 6: [6]}
BFS(G, 1)
