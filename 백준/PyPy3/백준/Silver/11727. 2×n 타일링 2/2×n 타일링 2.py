import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
dp = [0] * (x+1)
dp[0] = 1
dp[1] = 1
for i in range(2,x+1):
    dp[i] = dp[i-1] + 2*dp[i-2]
    dp[i] %= 10007

print(dp[x])