#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:divedeConquer.py
@time:2021/10/21
"""


def Rmaxmin(arr, i, j):
    if i == j:
        fmax, fmin = arr[i], arr[i]
        return fmax, fmin
    elif i == j - 1:
        if arr[i] < arr[j]:
            fmax, fmin = arr[j], arr[i]
        else:
            fmax, fmin = arr[i], arr[j]
        return fmax, fmin
    mid = (i + j) // 2
    gmax, gmin = Rmaxmin(arr, i, mid)
    hmax, hmin = Rmaxmin(arr, mid + 1, j)
    fmax = max(gmax, hmax)
    fmin = min(gmin, hmin)
    return fmax, fmin


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
    max, min = Rmaxmin(arr, 0, len(arr) - 1)
    print(max, min)
