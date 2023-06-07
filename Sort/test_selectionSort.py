import selectionSort
import random


def testsimple():
    assert selectionSort.selectionSort([1, 3, -7]) == [-7, 1, 3]


def testrandom():
    arr = []
    for i in range(1, 10):
        arr.append(random.randint(-100, 100))
    sorted_arr = sorted(arr)
    assert selectionSort.selectionSort(arr) == sorted_arr


def testwords():
    arr = ['ABC', 'ABB', 'abb', 'abc', 'xyz', 'xyz']
    sorted_arr = sorted(arr)
    assert selectionSort.selectionSort(arr) == sorted_arr
