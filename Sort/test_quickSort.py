import quickSort
import random


def testsimple():
    arr = [1, 3, -7]
    sorted_arr = sorted(arr)
    quickSort.quickSort(arr)
    assert arr == sorted_arr


def testrandom():
    arr = []
    for i in range(1, 10):
        arr.append(random.randint(-100, 100))
    sorted_arr = sorted(arr)
    quickSort.quickSort(arr)
    assert arr == sorted_arr


def testwords():
    arr = ['ABC', 'ABB', 'abb', 'abc', 'xyz', 'xyz']
    sorted_arr = sorted(arr)
    quickSort.quickSort(arr)
    assert arr == sorted_arr
