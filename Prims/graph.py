from collections import defaultdict


class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def add_edge(self, u, v, w):
        self.g[u].append((v, w))
        self.g[v].append((u, w))
