#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:countingSort.py
@time:2021/11/14
"""


def countingSort(A):
    k = max(A)
    C = [0 for i in range(k + 1)]
    for j in A:
        C[j] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    B = [0 for i in range(len(A))]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1

    return B


if __name__ == '__main__':
    arr = [3, 6, 4, 1, 3, 4, 1, 4]
    print(countingSort(arr))
