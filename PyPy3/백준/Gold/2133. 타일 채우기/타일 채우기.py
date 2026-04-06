import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
dp = [0 for i in range(n+1)]
if n > 1:
    dp[2] = 3
    for i in range(4, n+1,2):
        dp[i] = dp[i-2] * 3 + 2
        for j in range(4, i-1, 2):
            dp[i] += dp[i-j] * 2

print(dp[n])