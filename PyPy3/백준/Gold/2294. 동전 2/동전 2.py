import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [1e9 for i in range(k+1)]
for i in range(n):
    x = int(input())
    for j in range(1,k+1):
        if j % x == 0:
            dp[j] = min(dp[j], j // x)

        if j>=x:
            dp[j] = min(dp[j-x]+1, dp[j])

if dp[k] > 1e8:
    print(-1)
else:
    print(dp[k])