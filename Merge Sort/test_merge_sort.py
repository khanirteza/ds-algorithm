import pytest
from merge_sort import merge_sort

def test_random():
    arr = [9, 4, 8, 9, 2, 0]
    assert merge_sort(arr) == sorted(arr)

def test_empty_list():
    arr = []
    assert merge_sort(arr) == []

def test_rev():
    arr = [5, 4, 3, 2, 1]
    assert merge_sort(arr) == sorted(arr)

def test_sorted():
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == arr
    
def test_same():
    arr = [0, 0, 0, 0]
    assert merge_sort(arr) == arr

def test_one():
    arr = [1]
    assert merge_sort(arr) == arr

def test_two():
    arr = [2, -2]
    assert merge_sort(arr) == sorted(arr)