#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:quickSort.py
@time:2021/10/25
"""
import random
import sys

sys.setrecursionlimit(100000)  # 设置递归层数


def quicksort(arr, st, ed):
    if st == ed - 1 or st == ed:  # 递归出口
        return
    pivot = arr[st]  # 设置pivot
    firstgt = 0  # 第一个大于pivot的位置
    gt = 0  # 最后一个大于pivot的位置
    le = 0  # 最后一个小于pivot的位置
    for i in range(st + 1, ed):
        if arr[i] <= pivot:
            le = i
        if arr[i] > pivot:
            if firstgt == 0:
                firstgt = i
            gt = i
        if le > gt != 0:
            arr[le], arr[firstgt] = arr[firstgt], arr[le]
            le = firstgt
            firstgt += 1
            if i == ed - 1:
                arr[st], arr[firstgt - 1] = arr[firstgt - 1], arr[st]
                quicksort(arr, st, firstgt - 1)
                quicksort(arr, firstgt, ed)
                break
        if i == ed - 1 and le != 0:
            arr[st], arr[le] = arr[le], arr[st]
            quicksort(arr, st, le)
            quicksort(arr, le + 1, ed)
        if i == ed - 1 and le == 0:
            quicksort(arr, st + 1, ed)


if __name__ == '__main__':
    arr = [10, 7, 4, 9, 2, 4, 5, 1, 3, 8]
    # right = 0
    # wrong = 0
    # for epoch in range(100):
    #     for i in range(100):
    #         arr.append(random.randint(0, 1000))
    #     sortedarr = sorted(arr)
    #     quicksort(arr, 0, len(arr))
    #     if sortedarr == arr:
    #         right += 1
    #     else:
    #         wrong += 1
    #         print(arr)
    #         print(sortedarr)
    # arr = [5, 1, 3, 8, 7, 4, 6, 2]
    # input
    # while True:
    #     str = input()
    #     if str == 'q':
    #         break
    #     else:
    #         arr.append(int(str))

    print(arr)
    quicksort(arr, 0, len(arr))

    # print(sorted(arr))
    print(arr)
    # print(right)
    # print(wrong)
