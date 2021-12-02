#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:bucketSort.py
@time:2021/12/02
"""
from insertionSort import insertionSort


def bucketSort(arr, bucketNum):
    maxNum, minNum = max(arr), min(arr)
    bucketSize = (maxNum - minNum) / bucketNum
    buckets = [[] for _ in range(bucketNum)]
    result = []
    for i in range(len(arr)):
        index = (arr[i] - minNum) // bucketSize if arr[i] != maxNum else bucketNum - 1
        buckets[int(index)].append(arr[i])
    for j in range(len(buckets)):
        print(f"bucket{j} range:({minNum + j * bucketSize}, {minNum + (j + 1) * bucketSize}) : {buckets[j]})")
        insertionSort(buckets[j])
        print(f'after sort :  {buckets[j]}')
    for j in range(len(buckets)):
        result.extend(buckets[j])
    return result


if __name__ == '__main__':
    arr = [0.79, 0.31, 0.55, 0.4, 0.99, 0.78]
    print(bucketSort(arr, bucketNum=4))
