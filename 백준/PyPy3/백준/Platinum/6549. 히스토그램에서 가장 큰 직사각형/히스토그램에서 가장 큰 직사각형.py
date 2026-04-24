import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, *arr = map(int, input().split())
while(n != 0):
    q = [(arr[0],0)]
    area = 0
    lastv = min(arr)
    lasti = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            q.append((arr[i],i))
        elif arr[i] == arr[i-1]:
            continue
        else:
            t = q.pop()
            while (t[0] > arr[i]):
                area = max(area, t[0] *(i-t[1]))
                if len(q) == 0:
                    break
                lastv = t[0]
                lasti = t[1]
                t = q.pop()

            q.append((min(t[0], arr[i]), t[1]))
            q.append((arr[i], lasti))

    while(len(q) > 0):
        t = q.pop()
        area = max(area, t[0] * (n - t[1]))
    print(area)

    n, *arr = map(int, input().split())