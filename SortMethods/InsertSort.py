arr = [4, 7, 1, 5, 0, 9, 2, 10, 8, 6, 3]

def InsertSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(InsertSort(arr))

