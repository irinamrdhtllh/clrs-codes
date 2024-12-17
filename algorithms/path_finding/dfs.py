def DFS(G):
    visited = {}

    def DFSVisit(G, u):
        visited[u] = True
        print(u)
        for v in G[u]:
            if not visited.get(v, False):
                DFSVisit(G, v)

    for u in G:
        if not visited.get(u, False):
            DFSVisit(G, u)


G = {1: [2, 4], 2: [5], 3: [6, 5], 4: [2], 5: [4], 6: [6]}
DFS(G)
