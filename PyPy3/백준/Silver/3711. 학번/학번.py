import sys
import math
from collections import deque, Counter

times = int(input())
for time in range(times):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))

    isdone = False
    for i in range(1,10**6):
        rest = []
        for j in arr:
            if j%i in rest:
                break
            rest.append(j%i)
            if len(arr) == len(rest):
                isdone = True
                break
        if isdone:
            break

    print(i)