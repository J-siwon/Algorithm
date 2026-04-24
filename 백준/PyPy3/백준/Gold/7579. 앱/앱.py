import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n,m = map(int,input().split())
marr = list(map(int, input().split()))
carr = list(map(int,input().split()))
INF = int(1e9)
dp = [0 for i in range(sum(carr)+1)]

for i in range(n):
    now = marr[i]
    cost = carr[i]
    dp2 = dp[:]
    dp2[cost] = max(dp[cost], now)
    for i in range(cost, len(dp)):
        dp2[i] = max(dp[i-cost] + now, dp2[i])
    dp = dp2[:]

for i in range(len(dp)):
    if dp[i] >= m:
        print(i)
        break