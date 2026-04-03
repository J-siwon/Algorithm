import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n, k = map(int, input().split())
arr= list(map(int, input().split()))
dp = [0 for i in range(n+1)]
dp[0] = arr[0]
for i in range(1,len(arr)+1):
    dp[i] = dp[i-1] + arr[i-1]
t= -1e9
for i in range(n-k+1):
    t= max(t, dp[i+k] - dp[i])
print(t)