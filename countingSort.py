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
    arr = [1430, 3292, 7684, 1338, 193, 595, 4243, 9002, 4393, 130, 1001]
    print(countingSort(arr))
