import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    arr[i] = list(map(int,input().split()))

for i in range(int(input())):
    t = 0
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            t+= arr[i][j]
    print(t)