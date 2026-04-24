import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
low = 0
high = n-1
x = (0,0)
ans = (0,0)
minsum = 1e12
last = 0
while(low < high):
    t = arr[low] + arr[high]
    if  t>0:
        if minsum > abs(t):
            minsum = abs(t)
            x = (low, high)
            last = -1
        high -=1

    elif t <0:
        if minsum > abs(t):
            minsum = abs(t)
            x = (low, high)
            last = 1
        low += 1
    else:
        minsum = 0
        last = 0
        ans = (arr[low], arr[high])
        break

if last == 1:
    ans = (arr[x[0]], arr[x[1]])
elif last == -1:
    ans = (arr[x[0]], arr[x[1]])
print(*ans)