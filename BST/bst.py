class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
            return

        node = self.root
        while node:
            if data < node.data:
                if node.left is None:
                    node.left = self.Node(data)
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = self.Node(data)
                    return
                else:
                    node = node.right

    def search(self, data):
        node = self.root
        while node:
            if node.data == data:
                return True
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        return False

    def traverse(self, node):
        if node is not None:
            self.traverse(node.left)
            print(node.data)
            self.traverse(node.right)
    
    def min(self):
        node = self.root
        min = None
        while node:
            min = node.data
            node = node.left
        return min
    
    def max(self):
        node = self.root
        max = None
        while node:
            max = node.data
            node = node.right
        return max