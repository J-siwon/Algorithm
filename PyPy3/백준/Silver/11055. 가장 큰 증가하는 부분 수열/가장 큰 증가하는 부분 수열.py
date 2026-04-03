import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
arr = list(map(int, input().split()))

dp = [[arr[0], arr[0]]] #sum, maxa
ma = 0
for i in range(1,x):
    dp.append([arr[i], arr[i]])
    for j in dp:
        if j[1] < arr[i]: 
            dp[i][0] = max(dp[i][0], j[0] + arr[i])

for i in dp:
    ma = max(i[0], ma)
print(ma)