#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import log, sqrt
from multiprocessing import Process


EPS = .0000001

def sum_func(x):
    summ = x
    prev = 0
    i = 1
    while abs(summ - prev) > EPS:
        prev = summ
        summ += x ** (i * 2 + 1) / (i * 2 + 1)
        i += 1

    print(f"Sum is {summ}")


def check_func(x):
    res = log(sqrt((1 + x) / (1 - x)))
    print(f"Check: {res}")


if __name__ == '__main__':
    x = 0.35
    proc1 = Process(target=sum_func, args=(x,))
    proc2 = Process(target=check_func, args=(x,))
    proc1.start()
    proc2.start()
