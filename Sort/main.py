import sys
import time
from quickSort import quickSort
from selectionSort import selectionSort
from readfile import read
import gc
import random


def main():
    sys.setrecursionlimit(1000000)
    words = read()
    random.shuffle(words)
    n = [1000, 2000, 3000, 10000]
    selection_sort_times = []

    for number in n:
        copy_words = words[:number]
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        selectionSort(copy_words)
        stop = time.process_time()
        selection_sort_times.append(stop-start)
        if gc_old:
            gc.enable()


if __name__ == '__main__':
    main()
