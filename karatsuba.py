#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:karatsuba.py
@time:2021/09/10
"""


def karatsuba(x, y):
    xstr = str(x)
    ystr = str(y)
    xlen = len(xstr)
    ylen = len(ystr)
    maxLength = max(xlen, ylen)
    if xlen == 1 or ylen == 1:
        return x * y
    xstr = ''.join(list('0' * maxLength)[:-len(xstr)] + list(xstr))
    ystr = ''.join(list('0' * maxLength)[:-len(ystr)] + list(ystr))
    half = maxLength // 2
    a, b = int(xstr[:-half]), int(xstr[-half:])
    c, d = int(ystr[:-half]), int(ystr[-half:])
    q = karatsuba(a, c)
    p = karatsuba(b, d)
    k = karatsuba((a + b), (c + d))
    return 10 ** (2 * half) * q + 10 ** half * (k - q - p) + p


if __name__ == '__main__':
    c = karatsuba(123456789, 876543215)
    print(c)
    ans = 123456789 * 876543215
    print(ans)
