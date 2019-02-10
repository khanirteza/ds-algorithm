import pytest
from graph import Graph
from bfs import bfs

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(1, 6)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)


def test_bfs():
    assert bfs(g.g, 1) == [1, 2, 5, 6, 3, 4]
    assert bfs(g.g, 2) != [1, 2, 5, 6, 3, 4]
    assert bfs(g.g, 0) == []
    assert bfs(g.g, 6) == [6, 1, 2, 5, 3, 4]
