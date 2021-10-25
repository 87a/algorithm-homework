#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:selectionSort.py
@time:2021/10/05
"""

arr = []
# input
while True:
    str = input()
    if str == 'q':
        break
    else:
        arr.append(int(str))

print(arr)


def findmin(array, s, e):
    # function to find minimum element in array
    minIdx = s
    if s == e - 1:
        return s
    for i in range(s + 1, e):
        if array[i] < array[minIdx]:
            minIdx = i
    return minIdx


# print(findmin(arr, 0, len(arr)))
for i in range(0, len(arr)):
    # main loop
    minIndex = findmin(arr, i, len(arr))  # get the location of minimum
    arr[i], arr[minIndex] = arr[minIndex], arr[i]  # swap
    print(arr)
print(arr)
