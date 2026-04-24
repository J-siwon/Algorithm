import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
arr = [0]
for i in range(x):
    arr.append(int(input()))

#n번째를 밟을때 카운터가 [[1번째], [2번째]]

temp = [[0,0],[arr[1],0]]
for i in range(2,x+1):
    temp.append([max(temp[i-2])+arr[i], temp[i-1][0]+arr[i]])

print(max(temp[x]))