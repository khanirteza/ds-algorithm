def quick_sort(A, low, hi):
    if low < hi:
        pivot = partition(A, low, hi)
        quick_sort(A, low, pivot-1)
        quick_sort(A, pivot+1, hi)


def partition(A, low, hi):
    pivot = hi
    firstHi = low
    for i in range(low, hi):
        if A[i] < A[pivot]:
            A[i], A[firstHi] = A[firstHi], A[i]
            firstHi += 1
    
    A[pivot], A[firstHi] = A[firstHi], A[pivot]
    return firstHi