#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:insertionSort.py
@time:2021/09/20
"""
#
# arr = []
# # input
# while True:
#     str = input()
#     if str == 'q':
#         break
#     else:
#         arr.append(int(str))
#
# print(arr)


def insertionSort(arr):
    # if the array has only one element, there's no need to sort
    if len(arr) == 1:
        return
    else:
        # main loop
        for i in range(1, len(arr)):
            print(arr)
            # swap forward
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break
    return

if __name__ == '__main__':
    arr = [1430, 3292, 7684, 1338, 193, 595, 4243, 9002, 4393, 130, 1001]
    insertionSort(arr)
    print(arr)
