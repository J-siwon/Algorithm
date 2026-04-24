import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

times = int(input())
for time in range(times):
    n = int(input())
    arr = list(map(int, input().split()))
    sarr = [0 for i in range(n+1)]
    for i in range(1,n+1):
        sarr[i] = sarr[i-1] + arr[i-1]

    dp = [[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(1,n):
        for j in range(1,n-i+1):
            e = i+j
            s = sarr[e] - sarr[j-1]
            if dp[j][e] ==0:
                dp[j][e] = 1e9
            for k in range(j,e):
                dp[j][e] = min(dp[j][e], dp[j][k] + dp[k+1][e] + s)
    print(dp[1][n])