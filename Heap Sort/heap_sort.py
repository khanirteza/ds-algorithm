from heap import Heap

def heap_sort(arr):
    h = Heap(arr)
    for i in range(len(arr)):
        arr[i] = h.delete_min()