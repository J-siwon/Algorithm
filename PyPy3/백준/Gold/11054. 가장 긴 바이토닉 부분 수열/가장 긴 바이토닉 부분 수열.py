import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
arr= list(map(int, input().split()))


incdp = [[1, arr[0]]]
for i in range(1,x):
    incdp.append([1,arr[i]])
    for j in incdp:
        if j[1] < arr[i]:
            incdp[-1][0] = max(j[0]+1, incdp[-1][0])

arr.reverse()
decdp = [[1, arr[0]]]
for i in range(1,x):
    decdp.append([1,arr[i]])
    for j in decdp:
        if j[1] < arr[i]:
            decdp[-1][0] = max(j[0]+1, decdp[-1][0])
decdp.reverse()

ma = 0
for i in range(x):
    ma = max(incdp[i][0] + decdp[i][0]-1, ma)
print(ma)