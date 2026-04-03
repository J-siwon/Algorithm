import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())

dp = [i for i in range(n+1)]
t = int(n**0.5)
for i in range(2,t+1):
    x= i**2
    for j in range(1,n+1):
        if j%x == 0:
            dp[j] = min(dp[j], j//x)

        if j-i**2 >= 0:
            dp[j] = min(dp[j], dp[j-x] + 1)

print(dp[n])