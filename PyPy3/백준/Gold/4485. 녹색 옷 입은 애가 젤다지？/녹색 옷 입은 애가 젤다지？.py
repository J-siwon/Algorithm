import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

problem = 1
n = int(input())
while(n != 0):
    arr = [[] for i in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    arr2 = [[1e9 for i in range(n)] for i in range(n)]
    q = deque()
    q.appendleft((0,0))
    arr2[0][0] = arr[0][0]

    while(len(q)>0):
        t= q.pop()
        x = t[0]
        y = t[1]

        if x<n-1 and arr2[x+1][y] > arr2[x][y] + arr[x+1][y]:
            arr2[x+1][y] = arr2[x][y] + arr[x+1][y]
            q.appendleft((x+1,y))

        if x>0 and arr2[x-1][y] > arr2[x][y] + arr[x-1][y]:
            arr2[x-1][y] = arr2[x][y] + arr[x-1][y]
            q.appendleft((x-1,y))

        if y<n-1 and arr2[x][y+1] > arr2[x][y] + arr[x][y+1]:
            arr2[x][y+1] = arr2[x][y] + arr[x][y+1]
            q.appendleft((x,y+1))

        if y > 0 and arr2[x][y-1] > arr2[x][y] + arr[x][y-1]:
            arr2[x][y-1] = arr2[x][y] + arr[x][y-1]
            q.appendleft((x,y-1))

    print("Problem " + str(problem) + ": " + str(arr2[n-1][n-1]))
    problem += 1
    n = int(input())