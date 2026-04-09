import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    a,b = map(int, input().split())
    arr.append((a,b))

mat = [[(0,0) for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(i,n):
        if i==j:
            mat[i][j] =  arr[i]
        else:
            mat[i][j] = (arr[i][0], arr[j][1])


dp = [[0 for i in range(n)] for i in range(n)]

for i in range(1,n):
    for j in range(n-i):
        if dp[j][j+i] == 0:
            dp[j][j+i] = 1e9

        for k in range(j,j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + mat[j][k][0] * mat[j][k][1] * mat[k][j+i][1])
print(dp[0][-1])