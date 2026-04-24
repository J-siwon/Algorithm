import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())

arr = list(map(int, input().split()))
temp = [[0,0],[1,arr[0]]]

for i in range(x):
    if temp[-1][1] < arr[i]:
        temp.append([temp[-1][0] + 1, arr[i]])
    
    for j in range(1,len(temp)):
        if temp[j][1] > arr[i] > temp[j-1][1]:
            temp[j][1] = arr[i]

print(temp[-1][0])
        