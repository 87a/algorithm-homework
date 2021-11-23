#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:radixSort.py
@time:2021/11/23
"""


def countingSort(A, array):
    k = max(A)
    result = [0 for i in range(len(A))]
    C = [0 for i in range(k + 1)]
    for j in A:
        C[j] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    B = [0 for i in range(len(A))]
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        result[C[A[j]] - 1] = array[j]
        C[A[j]] -= 1

    return B, result


def radixSort(arr):
    maxLength = len(str(max(arr)))
    for i in range(1, maxLength + 1):
        arr_ = [int(str(arr[j])[-i]) if len(str(arr[j])) >= i else 0 for j in range(len(arr))]
        print(arr_)

        arr_sorted, arr = countingSort(arr_, arr)
        print(arr_sorted)
        print(arr)


if __name__ == '__main__':
    arr = [51, 7, 12, 336, 2, 67, 16, 553]
    radixSort(arr)
