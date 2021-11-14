#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:heapSort.py
@time:2021/10/30
"""
import random


def left(i):
    return 2 * (i + 1) - 1


def right(i):
    return 2 * (i + 1)


def parent(i):
    return (i + 1 // 2) - 1


def buildMaxHeap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        maxHeapify(arr, i, len(arr))


def maxHeapify(arr, i, heapsize):
    l, r = left(i), right(i)
    if l >= heapsize:
        return
    if arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest, heapsize)


def heapSort(arr):
    buildMaxHeap(arr)
    print(f"buildMaxHeap : {arr}")
    heapsize = len(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapsize -= 1
        maxHeapify(arr, 0, heapsize)
        print(f"{len(arr) - i} : {arr}")


if __name__ == '__main__':
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heapSort(arr)
