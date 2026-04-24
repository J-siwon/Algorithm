import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = ["N" for i in range(40001)]

for i in range(n):
    t= arr[i]
    dp2 = dp[:]
    dp2[t] = "Y"
    for j in range(1, len(dp)):
        if dp[j] == "Y":
            if j + t <= 40000:
                dp2[j+t] = "Y"
            dp2[abs(j-t)] = "Y"

    dp = dp2[:]

n = int(input())
for i in map(int,input().split()):
    print(dp[i], end = " ")
