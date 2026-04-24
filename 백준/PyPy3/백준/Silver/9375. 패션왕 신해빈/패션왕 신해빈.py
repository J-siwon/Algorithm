import sys
import math
from collections import deque, Counter

n = int(input())

for i in range(n):
    c = int(input())
    arr = dict()
    for j in range(c):
        a,b = input().split()
        if b in arr:
            arr[b].append(a)
        else:
            arr[b] = [a]

    t = []
    for j in arr:
        t.append(len(arr[j]))

    ad = 0
    for i in t:
        if ad == 0:
            ad = i+1
        else:
            ad *= i+1
    if ad != 0:
        print(ad-1)
    else:
        print(0)
