import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

v,e = map(int,input().split())

arr = [[1e9 for i in range(v)] for i in range(v)]
for i in range(e):
    a,b,w = map(int, input().split())
    w = abs(w-1)
    arr[a-1][b-1] = 0
    arr[b-1][a-1] = min(arr[b-1][a-1],w)

for i in range(v):
    arr[i][i] = 0
for k in range(v):
    for i in range(v):
        for j in range(v):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]


for times in range(int(input())):
    a,b = map(int, input().split())
    print(arr[a-1][b-1])