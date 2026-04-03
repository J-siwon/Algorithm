import sys
import math
from collections import deque
input = sys.stdin.readline


def BackTracking(arr, i, j):
    #check for 
    global isdone

    if isdone:
        return

    for r in range(9):
        if arr[i][r] == arr[i][j] and r != j:
            return
    for r in range(9):
        if arr[r][j] == arr[i][j] and r!= i:
            return

    ti = i%3
    tj = j%3
    for p in range(-ti,3-ti):
        for q in range(-tj, 3-tj):
            if p ==0 and q == 0:
                continue
            if arr[i+p][j+q] == arr[i][j]:
                return
            
    if len(tocheck) == 0:
        for i in range(9):
            print(*arr[i])
        isdone = True
        return

    for k in range(1,10):
        t = tocheck.pop()
        arr[t[0]][t[1]] = k
        BackTracking(arr, t[0], t[1])
        if isdone:
            return
        arr[t[0]][t[1]] = 0
        tocheck.append(t)


arr = []
isdone = False
tocheck = []
for i in range(9):
    arr.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            tocheck.append([i, j])

tocheck.reverse()
for k in range(1, 10):
    t = tocheck.pop()
    arr[t[0]][t[1]] = k
    BackTracking(arr, t[0], t[1])
    if isdone:
        break
    arr[t[0]][t[1]] = 0
    tocheck.append(t)