#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:bubbleSort.py
@time:2021/12/10
"""


def bubbleSortWithFlag(arr: list):
    time = len(arr)
    end = len(arr) - 1
    for i in range(0, time - 1):
        flag = False
        for j in range(0, end):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        # print(arr)
        if not flag:
            return arr
        end -= 1
    return arr


def bubbleSortWithInterval(arr: list):
    length = len(arr)
    interval = int(length // 1.3)
    while interval >= 1:
        i = 0
        while (i + interval) < length:
            if arr[i] > arr[i + interval]:
                arr[i], arr[i + interval] = arr[i + interval], arr[i]
            i += 1
        interval = int(interval // 1.3)
    return arr


if __name__ == '__main__':
    arr = [3, 1, 5, 9, 7, 4, 6, 10, 20, 2, 8]
    print(bubbleSortWithFlag(arr))
    print(bubbleSortWithInterval(arr))
