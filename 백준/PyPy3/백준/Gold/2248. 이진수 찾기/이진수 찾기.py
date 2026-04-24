import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n,k,l = map(int, input().split())

dp = [[0 for i in range(n+1)]for i in range(k+1)]

for i in range(k+1):
    dp[i][0] = 1

for i in range(n+1):
    dp[0][i] = 1

for i in range(1,k+1):
    for j in range(1,n+1):
        dp[i][j] = min(2**j, dp[i][j-1] + dp[i-1][j-1])

bitnow = n
left = l
oneleft = k
ans = ""
while bitnow>0:
    if oneleft == 0:
        ans += "0"
        left -= 1
        bitnow -= 1
        continue

    if dp[oneleft][bitnow-1] < left:
        ans += "1"
        left -= dp[oneleft][bitnow-1]
        oneleft -= 1
        bitnow -= 1
    else:
        ans += "0"
        bitnow -= 1

print(ans)