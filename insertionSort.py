#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:insertionSort.py
@time:2021/09/20
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

# if the array has only one element, there's no need to sort
if len(arr) == 1:
    print(arr)
else:
    # main loop
    for i in range(1, len(arr)):
        # swap forward
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
print(arr)
