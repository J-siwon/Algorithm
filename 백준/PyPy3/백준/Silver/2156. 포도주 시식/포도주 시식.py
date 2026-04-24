import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
arr = [0]
for i in range(x):
    arr.append(int(input()))

#n번째를 마실때 카운터가 [[1번째], [2번째]]
temp = [[0,0], [6,0], [10,16], [19, 23], []]

maxcounter = 0
temp = [[0,0],[arr[1],0]]
for i in range(2,x+1):
    maxcounter = max(maxcounter, max(temp[i-2]))
    temp.append([maxcounter+arr[i], temp[i-1][0]+arr[i]])

ans = 0
for i in range(x+1):
    for j in range(2):
        ans = max(ans, temp[i][j])

print(ans)