import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0 for i in range(n)] for i in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1
arr2 = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    arr2[i] = arr[i].copy()
for i in range(n):
    arr2[i][i] = 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            arr2[j][i] = 1

count = 0
for i in range(n):
    if min(arr2[i]) == 1:
        count +=1

print(count)