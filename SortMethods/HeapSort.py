l = [47, 35, 60, 95, 77, 15, 28]

def adjust(pos, n, arr):
    temp = arr[pos]
    child = pos * 2 + 1
    while child <= n:
        if child + 1 <= n and arr[child] < arr[child + 1]:
            child = child + 1
        if temp > arr[child]:
            break
        arr[pos] = arr[child]
        pos = child
        child = pos * 2 + 1
    arr[pos] = temp


def heapSort(arr):
    #build heap
    n = len(arr) - 1
    for i in range((n-1)//2, -1, -1):
        adjust(i, n, arr)
    #sort ascending order
    for i in range(n, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        adjust(0, i - 1, arr)


heapSort(l)

for i in l:
    print(i, end = " ")