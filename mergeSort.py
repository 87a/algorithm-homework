#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:mergeSort.py
@time:2021/10/14
"""


def merge(left, right):
    # 将左右两段合并
    result = []  # 用于存储结果
    i, j = 0, 0  # 下标
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 小的元素优先放入数组中
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 放入余下的元素
    result += left[i:]
    result += right[j:]
    # print(result)
    return result


def mergeSort(array):
    # 归并排序
    if len(array) == 1:  # 递归出口,只有一个元素
        return array
    mid = len(array) // 2
    # 递归将左右两半进行排序
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left, right)


if __name__ == '__main__':
    arr = []
    # input
    while True:
        str = input()
        if str == 'q':
            break
        else:
            arr.append(int(str))

    print(arr)
    res = mergeSort(arr)
    print(res)
