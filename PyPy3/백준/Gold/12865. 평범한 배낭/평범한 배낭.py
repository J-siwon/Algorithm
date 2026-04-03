import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0 for i in range(k+1)]

for i in range(n):
    w, v = map(int, input().split())
    dp2 = [0 for i in range(k+1)]
    for j in range(0,len(dp2)-w):
        dp2[w+j] = v + dp[j]

    for j in range(len(dp)):
        dp[j] = max(dp[j], dp2[j])
    
    
print(dp[k])