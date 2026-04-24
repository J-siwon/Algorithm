import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

v,e = map(int, input().split())

arr = [[1e9 for i in range(v)] for i in range(v)]

for i in range(e):
    a,b,w = map(int, input().split())
    arr[a-1][b-1] = w

mind = 1e9
for k in range(v):
    for i in range(v):
        for j in range(v):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(v):
    for j in range(v):
        if i == j:
            continue
        mind = min(mind, arr[i][j] + arr[j][i])


if mind > 1e8:
    print(-1)
else:
    print(mind)