class Heap:
    def __init__(self, arr=[]):
        self.heap = []
        for i in arr:
            self.insert(i)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up()
    
    def delete_min(self):
        ret = self.get_min()
        if ret:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self.heap.pop()
            self.heapify_down()
        return ret

    def heapify_up(self):
        i = len(self.heap) - 1
        parent = (i-1) // 2
        while i and self.heap[parent] > self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent
            parent = (i-1) // 2

    def heapify_down(self):
        i = 0
        c1 = 2*i + 1
        c2 = 2*i + 2
        while c1 < len(self.heap) or c2 < len(self.heap):
            if c2 < len(self.heap):
                if self.heap[i] <= self.heap[c1] and self.heap[i] <= self.heap[c2]:
                    return
                c = self.swap(i, c1, c2)
                i = c
                c1 = 2*i + 1
                c2 = 2*i + 2
            else:
                if self.heap[i] > self.heap[c1]:
                    self.heap[i], self.heap[c1] = self.heap[c1], self.heap[i]
                return
    
    def swap(self, i, c1, c2):
        if self.heap[c1] < self.heap[c2]:
            self.heap[i], self.heap[c1] = self.heap[c1], self.heap[i]
            return c1
        else:
            self.heap[i], self.heap[c2] = self.heap[c2], self.heap[i]
            return c2
