import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n,k = map(int, input().split())
dp = [[0 for i in range(n+1)] for i in range(k+1)]
dp[0][0] = 1
for i in range(1,k+1):
    dp[i] = dp[i-1][:]
    for k in range(1,n+1):
        for j in range(k,n+1):
            dp[i][j] += dp[i-1][j-k]

    for k in range(n+1):
        dp[i][k] %= 1000000000

print(dp[-1][-1])