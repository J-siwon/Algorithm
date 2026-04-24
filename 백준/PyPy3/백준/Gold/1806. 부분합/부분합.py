import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int, input().split()))

dp = [0 for i in range(n+1)]
for i in range(1,n+1):
    dp[i] = dp[i-1] +arr[i-1]

isdone = False
minlen = 1e9
for i in range(1,n+1):
    low = i
    high = n
    if dp[-1] - dp[i-1] < m:
        continue
    while(low < high):
        t = (low + high) //2
        if dp[t] >= m + dp[i-1]:
            high = t
        else:
            low = t+1
    minlen = min(minlen, low - i+1)

if minlen > 1e8:
    print(0)
else:
    print(minlen)