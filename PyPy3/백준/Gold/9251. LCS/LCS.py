import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

x = list(input().strip())
y = list(input().strip())

arr = [[0 for i in range(len(y))] for j in range(len(x))] 

if len(x)>0 and len(y)>0 :
    if x[0] == y[0]:
        arr[0][0] = 1

    for i in range(1,len(x)):
        if x[i] == y[0] or arr[i-1][0] == 1:
            arr[i][0] = 1
    for i in range(1,len(y)):
        if x[0] == y[i] or arr[0][i-1] == 1:
            arr[0][i] = 1


    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i] == y[j]:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i-1][j-1], arr[i][j-1])

if len(x) == 0 or len(y) == 0:
    print(0)
else:
    print(arr[-1][-1])