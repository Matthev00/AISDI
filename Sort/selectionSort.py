def selectionSort(arr):
    n = len(arr)
    for index in range(n):
        minIndex = index
        for j in range(minIndex+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[minIndex], arr[index] = arr[index], arr[minIndex]
    return arr
