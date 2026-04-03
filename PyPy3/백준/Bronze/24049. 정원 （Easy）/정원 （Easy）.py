import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [[0 for i in range(n+1)] for i in range(m+1)]
arr[0] = [0] + list(map(int, input().split()))
tarr = [0] + list(map(int, input().split()))
for i in range(len(tarr)):
    arr[i][0] = tarr[i]

for i in range(1,len(arr)):
    for j in range(1,len(arr[0])):
        if arr[i-1][j] == arr[i][j-1]:
            arr[i][j] = 0
        else:
            arr[i][j] = 1
print(arr[-1][-1])