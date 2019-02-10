import pytest
from graph import Graph
from dfs import DFS

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(1, 6)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)


def test_dfs():
    dfs = DFS()
    dfs.traverse(g.g, 1)
    assert dfs.early_vertex == [1, 2, 3, 4, 5, 6]
    
