class DFS:
    def __init__(self):
        self.discovered = set()
        self.processed = set()
        self.parent = {}
        self.early_vertex = []
        self.edges = []

    def process_edge(self, u, v):
        self.edges.append((u, v))

    def process_vertex_early(self, u):
        self.early_vertex.append(u)

    def traverse(self, G, u):
        self.discovered.add(u)
        self.process_vertex_early(u)
        for v in G[u]:
            if v not in self.discovered:
                self.parent[v] = u
                self.process_edge(u, v)
                self.traverse(G, v)
            elif v not in self.processed:
                self.process_edge(u, v)
        self.processed.add(u)
