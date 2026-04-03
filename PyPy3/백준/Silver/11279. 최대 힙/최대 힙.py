import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    if x==0:
        if len(arr) ==0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -x)