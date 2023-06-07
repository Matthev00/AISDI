def quickSort(arr, leftIndex=0, rightIndex=None):
    if not rightIndex:
        rightIndex = len(arr) - 1
    if leftIndex < rightIndex:
        pivotIndex = partition(arr, leftIndex, rightIndex)
        quickSort(arr, pivotIndex+1, rightIndex)
        quickSort(arr, leftIndex, pivotIndex-1)


def partition(arr, leftIndex, rightIndex):
    pivotElement = arr[rightIndex]
    i = leftIndex
    for j in range(leftIndex, rightIndex):
        if arr[j] <= pivotElement:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[rightIndex], arr[i] = arr[i], arr[rightIndex]
    return i