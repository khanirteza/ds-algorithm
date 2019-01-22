import pytest
from binary_search import binary_search

arr = [-83, -59, 0, 2, 3, 8, 19, 22, 29, 30, 30, 112]

def test_search():
    assert binary_search(arr, 0, 0, len(arr)-1) == True
    assert binary_search(arr, 3923, 0, len(arr)-1) == False
    assert binary_search(arr, -323, 0, len(arr)-1) == False
    assert binary_search(arr, 1, 0, len(arr)-1) == False
    assert binary_search(arr, 2, 0, len(arr)-1) == True
    assert binary_search(arr, 21, 0, len(arr)-1) == False
    assert binary_search(arr, 30, 0, len(arr)-1) == True

def test_empty_list():
    empt = []
    assert binary_search(empt, 0, 0, 0) == False