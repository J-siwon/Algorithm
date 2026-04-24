import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
arr= list(map(int, input().split()))

dp = [[1, arr[0]]] #길이, 최소
for i in range(1,x):
    dp.append([1,arr[i]])
    for j in dp:
        if j[1] > arr[i]:
            dp[-1][0] = max(j[0]+1, dp[-1][0])

ma = 0
for i in dp:
    ma = max(i[0], ma)
print(ma)