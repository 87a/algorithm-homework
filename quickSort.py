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


def quickSort(arr, left, right):
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    for i in range(index, right + 1):
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1

    arr[pivot], arr[index - 1] = arr[index - 1], arr[pivot]
    return index - 1


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
quickSort(arr, 0, len(arr) - 1)

# print(sorted(arr))
print(arr)
# print(right)
# print(wrong)
