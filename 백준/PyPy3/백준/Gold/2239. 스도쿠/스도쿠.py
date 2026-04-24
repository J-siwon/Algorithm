import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def dfs(x):
    global isdone
    if isdone:
        return

    i = x//9
    j = x%9
    if x==81:
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end = "")
            print()
        isdone = True
        return
    if arr[i][j] != 0:
        dfs(x+1)
        return

    for k in range(1, 10):
        skip = False
        for q in range(9):
            if arr[i][q] == k:
                skip = True
                break

        for q in range(9):
            if arr[q][j] == k:
                skip = True
                break

        for p in range((i // 3) * 3, (i // 3) * 3 + 3):
            for q in range((j // 3) * 3, (j // 3) * 3 + 3):
                if arr[p][q] == k:
                    skip = True
                    break
            if skip:
                break

        if not skip:
            arr[i][j] = k
            dfs(x+1)
            arr[i][j] = 0

arr = [[0 for i in range(9)] for i in range(9)]
isdone = False
for i in range(9):
    arr[i] = list(input().strip())
    for j in range(9):
        arr[i][j] = int(arr[i][j])

dfs(0)