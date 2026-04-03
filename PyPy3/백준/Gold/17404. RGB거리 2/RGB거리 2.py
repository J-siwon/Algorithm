import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
if n==2:
    a,b,c = map(int, input().split())
    r,g,b2= map(int, input().split())
    print(min(a+g, b+b2, c+r, a+b2, b+r, c+g))
else:
    dp = [(0,0,0) for i in range(n)]
    dp2 = [(0,0,0) for i in range(n)]
    dp3 = [(0, 0, 0) for i in range(n)]

    r,g,b = map(int, input().split())

    dp[0] = (1e9,g,b)
    dp2[0] = (r,1e9,b)
    dp3[0] = (r, g, 1e9)
    for i in range(1,n):
        r,g,b = map(int, input().split())
        dp[i] = (min(dp[i-1][1], dp[i-1][2])+r, min(dp[i-1][0], dp[i-1][2])+g, min(dp[i-1][0], dp[i-1][1])+b)
        dp2[i] = (min(dp2[i-1][1], dp2[i-1][2])+r, min(dp2[i-1][0], dp2[i-1][2])+g, min(dp2[i-1][0], dp2[i-1][1])+b)
        dp3[i] = (min(dp3[i - 1][1], dp3[i - 1][2]) + r, min(dp3[i - 1][0], dp3[i - 1][2]) + g,
                  min(dp3[i - 1][0], dp3[i - 1][1]) + b)

    print(min(dp[-1][0], dp2[-1][1], dp3[-1][2]))