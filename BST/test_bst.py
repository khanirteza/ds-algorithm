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
    assert bst.search(53) == True
    assert bst.search(0) == False
    assert bst.search(22) == False
    assert bst.search(54) == True
    assert bst.search(3) == True
    assert bst.search(87) == True
    assert bst.search(1) == True
    assert bst.search(1) == True
    assert bst.search(99) == False

def test_min():
    assert bst.min() == -23

def test_max():
    assert bst.max() == 100
