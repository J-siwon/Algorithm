import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n,k = map(int, input().split())

arr = [[0 for i in range(n)] for i in range(n)]
for i in range(k):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] ==1 and arr[k][j] == 1:
                arr[i][j] = 1

times = int(input())
for times in range(times):
    a,b = map(int, input().split())
    if arr[a-1][b-1] == 1 and arr[b-1][a-1] == 1:
        print(0)
    elif arr[a-1][b-1] == 1 and arr[b-1][a-1] == 0:
        print(-1)
    elif arr[a-1][b-1] == 0 and arr[b-1][a-1] == 1:
        print(1)
    else:
        print(0)
