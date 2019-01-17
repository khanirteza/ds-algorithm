from trie import Trie

tr = Trie()

tr.insert("helLO")
tr.insert("Hi")
tr.insert("world")
tr.insert("wonder")
tr.insert("python")
tr.insert("pascal")

def test_seart():
    assert tr.search("Hello") == True
    assert tr.search("Hifi") == False
    assert tr.search("Java") == False
    assert tr.search("pYThOn") == True
    assert tr.search("algorithm") == False
    assert tr.search("wor") == False