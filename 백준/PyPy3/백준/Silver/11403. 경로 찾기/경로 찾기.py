import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = [[] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            q.appendleft((i,j))

while(len(q) >0):
    t= q.pop()
    i = t[0]
    j = t[1]

    for k in range(n):
        if arr[i][k] == 0 and arr[j][k] == 1:
            arr[i][k] = 1
            q.appendleft((i,k))


for i in range(n):
    print(*arr[i])