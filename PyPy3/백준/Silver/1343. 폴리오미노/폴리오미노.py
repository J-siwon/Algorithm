import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

s = input().strip()
arr = list(s.split('.'))
isdone = False
for i in arr:
    if len(i) %2 != 0:
        isdone = True
        print(-1)
        break

for i in range(len(arr)):
    if len(arr[i]) % 4 == 0:
        arr[i] = "A"*len(arr[i])
    else:
        arr[i] = "A" * (len(arr[i])-2) + "B"*2

if not isdone:
    for i in range(len(arr)-1):
        print(arr[i], end = ".")
    print(arr[-1])