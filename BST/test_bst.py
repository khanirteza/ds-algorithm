import pytest
from bst import BST

bst = BST()

bst.insert(53)
bst.insert(5)
bst.insert(87)
bst.insert(53)
bst.insert(1)
bst.insert(-23)
bst.insert(100)
bst.insert(50)
bst.insert(54)
bst.insert(2)
bst.insert(3)


def test_traverse(capsys):
    bst.traverse(bst.root)
    captured = capsys.readouterr()
    assert captured.out == "-23\n1\n2\n3\n5\n50\n53\n53\n54\n87\n100\n"

def test_search():
    assert bst.search(53).data == 53
    assert bst.search(0) == None
    assert bst.search(22) == None
    assert bst.search(54).data == 54
    assert bst.search(3).data == 3
    assert bst.search(87).data == 87
    assert bst.search(1).data == 1
    assert bst.search(1).data == 1
    assert bst.search(99) == None

def test_min():
    assert bst.get_min_node().data == -23
    assert bst.get_min_node().data != 1

def test_max():
    assert bst.get_max_node().data == 100
