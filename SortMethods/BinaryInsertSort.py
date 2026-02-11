arr = [4, 7, 1, 5, 0, 9, 2, 10, 8, 6, 3]

def BIS(arr):
    for i in range(1, len(arr)):
        low = 0
        high = i-1
        while low <= high:
            mid = int((low + high) / 2)
            if arr[i] >= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        key = arr[i]
        for j in range(i, low, -1):
            arr[j] = arr[j - 1]
        arr[low] = key
    return arr
print(BIS(arr))
