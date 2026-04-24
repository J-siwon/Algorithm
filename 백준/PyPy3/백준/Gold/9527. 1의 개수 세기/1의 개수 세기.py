import heapq
import sys
import math
from collections import deque
input = sys.stdin.readline

def log2(x):
    z = 0
    while(2**z<= x):
        z+=1
    return z-1

def Get(x):
    if x <= 2:
        return x
    if x == 3:
        return 4

    t = log2(x)
    if x - 2**t == 0:
        return dp[t]+1

    return dp[t] + Get(x- 2**t) + x-2**t+1

n,m = map(int, input().split())
t= log2(m)
dp = [0 for i in range(max(t+1, 3))]
dp[1] = 1
dp[2] = 4
for i in range(3,t+1):
    dp[i] = Get(2**i-1)

print(Get(m)- Get(n-1))