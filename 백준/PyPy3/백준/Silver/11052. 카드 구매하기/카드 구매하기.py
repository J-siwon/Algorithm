import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
arr = []
for i in range(len(t)):
    arr.append([i+1,t[i]])
arr = sorted(arr, key= lambda x: x[1]/x[0], reverse= True)

dp = [0 for i in range(n+1)]

for i in range(n):
    num = arr[i][0]
    value = arr[i][1]
    dp[num] = max(dp[num], value)
    for j in range(len(dp)):
        if j-num>=0:
            dp[j] = max(dp[j-num] + value, dp[j])
print(dp[n])
