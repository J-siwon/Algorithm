import sys
import math
from collections import deque, Counter

n = int(input())
dp = [0 for i in range(50001)]

for i in range(1,224):
    t= i**2
    dp[t] = 1
    for j in range(len(dp)-t):
        if dp[j] != 0:
            if dp[j+t] == 0:
                dp[j+t] = dp[j] + 1
            else:
                dp[j+t] = min(dp[j] + 1, dp[j+t])

print(dp[n])