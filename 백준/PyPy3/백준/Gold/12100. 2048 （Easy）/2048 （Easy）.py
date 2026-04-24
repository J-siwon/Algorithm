import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def Move(arr, k,depth):
    global ans
    if depth == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, arr[i][j])
        return
    toswitch = []
    tempc = 1
    for j in range(startx[k], endx[k],stepx[k]):
        for i in range(starty[k], endy[k], stepy[k]):
            if arr[i][j] == 0:
                continue

            tempx= j
            tempy = i
            while(True):
                if tempx == startx[k] and dx[k] != 0:
                    break
                if tempy == starty[k] and dy[k] != 0:
                    break

                if arr[tempy+dy[k]][tempx+dx[k]] == arr[tempy][tempx]:
                    arr[tempy][tempx] = 0
                    toswitch.append((tempy+dy[k], tempx+dx[k], arr[tempy+dy[k]][tempx+dx[k]]*2))
                    arr[tempy + dy[k]][tempx + dx[k]] = -tempc
                    tempc+=1
                    break
                elif arr[tempy+dy[k]][tempx+dx[k]] == 0:
                    arr[tempy + dy[k]][tempx + dx[k]] = arr[tempy][tempx]
                    arr[tempy][tempx] = 0
                else:
                    break

                tempx += dx[k]
                tempy += dy[k]

    for x in toswitch:
        arr[x[0]][x[1]] = x[2]

    for i in range(4):
        temparr = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            for q in range(n):
                temparr[j][q] = arr[j][q]
        Move(temparr, i, depth +1)

n = int(input())

dx= [1,-1,0,0]
dy= [0,0,1,-1]
startx = [n-1, 0, 0,0]
endx = [-1,n,n,n]
starty = [0,0,n-1,0]
endy= [n,n,-1,n]
stepx = [-1,1,1,1]
stepy = [1,1,-1,1]

originarr = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    originarr[i] = list(map(int,input().split()))
ans = 0
for i in range(4):
    temparr = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            temparr[j][k] = originarr[j][k]
    Move(temparr, i, 0)

print(ans)