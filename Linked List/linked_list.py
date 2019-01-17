class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.root = None
    
    def append(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            curr = self.root
            while curr.next:
                curr = curr.next
            curr.next = self.Node(data)
    
    def traverse(self):
        curr = self.root
        while curr:
            print(curr.data)
            curr = curr.next
    
    def get_data(self, index):
        curr = self.root
        cnt = 0
        while curr:
            if cnt == index:
                return curr.data
            curr = curr.next
            cnt += 1
        return None
    
    def delete(self, index):
        curr = self.root
        if self.root is None:
            return False
        if index == 0:
            self.root = self.root.next
            return True

        prev = curr
        curr = curr.next
        cnt = 1
        while curr:
            if cnt == index:
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
            cnt += 1
        
        return False
