def binary_search(arr, key, low, high):
    if low > high or arr == []:
        return False
    mid = (low + high) // 2
    if arr[mid] == key:
        return True
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid-1)
    else:
        return binary_search(arr, key, mid+1, high)
