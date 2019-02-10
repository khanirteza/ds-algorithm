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
