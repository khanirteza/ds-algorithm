import heapq
from graph import Graph


def get_prims_mst(G, s):
    T = Graph()
    vNew = set()
    vNew.add(s)
    hp = []
    for v, w in G[s]:
        heapq.heappush(hp, (w, s, v))
    
    while len(vNew) < len(G):
        w, u, v = heapq.heappop(hp)
        if v not in vNew:
            T.add_edge(u, v, w)
            vNew.add(v)
            for vn, wn in G[v]:
                heapq.heappush(hp, (wn, v, vn))
    
    return T