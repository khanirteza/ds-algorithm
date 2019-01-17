class Trie:
    class Node:
        def __init__(self):
            self.endmark = False
            self.next = {}
    
    def __init__(self):
        self.root = self.Node()
    
    def insert(self, str):
        str = str.lower()
        curr = self.root
        for c in str:
            if c not in curr.next:
                curr.next[c] = self.Node()
            curr = curr.next[c]
        curr.endmark = True

    def search(self, str):
        str = str.lower()
        curr = self.root
        for c in str:
            if c not in curr.next:
                return False
            curr = curr.next[c]
        return curr.endmark