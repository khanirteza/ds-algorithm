from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def add_edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

def bfs(G, s):
    if s not in G:
        return []
    visited = {s}
    q = [s]
    result = []
    while q:
        u = q.pop(0)
        result.append(u)
        for v in G[u]:
            if v not in visited:
                q.append(v)
                visited.add(v)
    return result