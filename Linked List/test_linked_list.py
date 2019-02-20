import pytest
from linked_list import LinkedList

def test_append(capsys):
    ll = LinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(9)
    ll.traverse()
    captured = capsys.readouterr()
    assert captured.out == "3\n5\n9\n"

def test_get_data(capsys):
    ll = LinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(9)
    assert ll.get_data(0) == 3
    assert ll.get_data(1) != 6
    assert ll.get_data(10) == None

def test_delete(capsys):
    ll = LinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(9)
    assert ll.delete(3) == False
    assert ll.delete(0) == True
    ll.traverse()
    captured = capsys.readouterr()
    assert captured.out == "5\n9\n"

def test_reverse(capsys):
    ll = LinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(9)
    ll.reverse(ll.root)
    ll.traverse()
    captured = capsys.readouterr()
    assert captured.out == "9\n5\n3\n"
