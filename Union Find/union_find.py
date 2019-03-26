class UnionFind:
    def __init__(self):
        self.parent = dict()

    def find(self, r):
        if r not in self.parent or r == self.parent[r]:
            self.parent[r] = r
            return r
        self.parent[r] = self.find(self.parent[r])
        return self.parent[r]

    def union(self, a, b):
        u = self.find(a)
        v = self.find(b)
        self.parent[v] = u
