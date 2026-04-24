import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
if n%2 == 0:
    dp = [0 for i in range(n)]
    for i in range(1,n//2+1):
        if i==1:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] * 2
    print(dp[n//2])
else:
    print(0)