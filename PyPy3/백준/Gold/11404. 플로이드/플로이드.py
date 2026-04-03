import sys
import math
import heapq
from collections import deque, Counter

n = int(input())
m = int(input())
arr = [[1e9 for i in range(n)] for i in range(n)]
for i in range(m):
    a,b,w = map(int, input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], w)

for mid in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > arr[i][mid] + arr[mid][j]:
                arr[i][j] = arr[i][mid] + arr[mid][j]

for i in range(n):
    arr[i][i] = 0
    for j in range(n):
        if arr[i][j] > 1e8:
            arr[i][j] = 0

for i in arr:
    print(*i)