import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [arr[i]%m for i in range(len(arr))]

for i in range(1,len(dp)):
    dp[i] = dp[i-1] + arr[i]%m

for i in range(len(dp)):
    dp[i] = dp[i] % m

count = 0
c = Counter(dp)
c[0] += 1
for i in c:
    x = c[i]
    count += x*(x-1)//2

print(count)