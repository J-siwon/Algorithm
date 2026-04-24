import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n,k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort()
coins.reverse()
dp = [[0 for i in range(k+1)] for i in range(n+1)]

for i in range(1,n+1):
    t = coins[i-1]
    dp[i] = dp[i-1][:]
    dp[i][0] = 1
    for j in range(t, k+1):
        dp[i][j] = max(dp[i][j], dp[i][j-t] + dp[i-1][j])

print(dp[n][-1])