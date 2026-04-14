import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
dp = [0 for i in range(n)]
dp2 = [0 for i in range(n)]
dp[0] = 1
dp2[0] = 1
for i in range(1,n):
    dp[i] = (dp[i-1] + 2 * dp2[i-1])
    dp2[i] = (dp[i-1] + dp2[i-1])
    dp[i] %= 9901
    dp2[i] %= 9901

print((dp[-1] + 2 * dp2[-1]) % 9901)