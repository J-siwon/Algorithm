import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

arr = []
for i in range(int(input())):
    a,b = map(int, input().split())
    arr.append([a,b])
arr = sorted(arr)

arr2 = []
for i in range(len(arr)):
    arr2.append(arr[i][1])

arr = arr2
arr2 = [[0,0]]
for i in range(1,len(arr)+1):
    if arr2[-1][1] < arr[i-1]:
        arr2.append([arr2[-1][0]+1, arr[i-1]])
    else:
        for j in range(1, len(arr2)):
            if arr2[j-1][1] < arr[i-1] < arr2[j][1]:
                arr2[j][1] = arr[i-1]
print(len(arr) - arr2[-1][0])