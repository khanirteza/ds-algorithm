def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = merge_sort(arr[:mid])
        R = merge_sort(arr[mid:])
        arr = merge(L, R)
    return arr

def merge(L, R):
    i = j = 0
    arr = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr.append(L[i])
            i += 1
        else:
            arr.append(R[j])
            j += 1
    while i < len(L):
        arr.append(L[i])
        i += 1
    while j < len(R):
        arr.append(R[j])
        j += 1
    return arr