#二分
arr = [2, 7, 15, 25, 33, 39, 48, 51, 60, 76, 80, 99]

def binarySearch(arr, value):
    low = 0
    high = len(arr) - 1
    mid = int((low + high) / 2)
    while(low <= high):
        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            return mid
        mid = int((low + high) / 2)
    return -1

print(binarySearch(arr, 99))