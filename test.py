#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    li = {}
    for num in ar:
        li[num] = int(li.get(num, 0)) + 1
    print(li)
    pairs = []
    for key in li.keys():
        a = int(li[key]) // 2
        pairs.append(a)

    return sum(pairs)


if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
