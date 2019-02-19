import pytest
from quick_sort import quick_sort


def test_random():
    arr = [9, 4, 8, 9, 2, 0]
    quick_sort(arr, 0, len(arr)-1)
    assert arr == [0, 2, 4, 8, 9, 9]


def test_empty_list():
    arr = []
    quick_sort(arr, 0, len(arr)-1)
    assert arr == []


def test_rev():
    arr = [5, 4, 3, 2, 1]
    quick_sort(arr, 0, len(arr)-1)
    assert arr == [1, 2, 3, 4, 5]


def test_sorted():
    arr = [1, 2, 3, 4, 5]
    quick_sort(arr, 0, len(arr)-1)
    assert arr == [1, 2, 3, 4, 5]


def test_same():
    arr = [0, 0, 0, 0]
    quick_sort(arr, 0, len(arr)-1)
    assert arr == [0, 0, 0, 0]


def test_one():
    arr = [1]
    quick_sort(arr, 0, len(arr)-1)
    assert arr == [1]


def test_two():
    arr = [2, -2]
    quick_sort(arr, 0, len(arr)-1)
    assert arr == [-2, 2]
