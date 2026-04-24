import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(10**5)

n,m = map(int, input().split())
arr = [[]for i in range(n)]
for i in range(n):
    arr[i] = list(input().strip())

for i in range(n):
    for j in range(m):
        arr[i][j] = int(arr[i][j])

ct = [[[1e9,True] for i in range(m)] for i in range(n)]
count = 0
breakable = True
tovisit = deque()
unbreakable = False

ct[0][0][0] = 0
if n>1:
    if arr[1][0] == 1:
        tovisit.append([1,0,False])
    else:
        tovisit.append([1, 0, True,])
    ct[1][0][0] = 1
if m>1:
    if arr[0][1] == 1:
        tovisit.append([0,1,False])
    else:
        tovisit.append([0, 1, True])
    ct[0][1][0] = 1

while(len(tovisit) > 0):
    t = tovisit.popleft()
    i = t[0]
    j = t[1]
    breakable = t[2]
    count = ct[i][j][0]

    if i==n-1 and j == m-1:
        break

    if i < n-1:
        if breakable:
            if ct[i+1][j][1] == False and arr[i+1][j] == 0:
                tovisit.append([i+1,j,True])
                ct[i+1][j][0] = count+1
                ct[i+1][j][1] = True
            elif arr[i+1][j] == 1:
                if ct[i+1][j][0] > count+1:
                    tovisit.append([i+1,j,False])
                    ct[i+1][j][0] = count+1
                    ct[i+1][j][1] = False
            else:
                if ct[i + 1][j][0] > count + 1:
                    tovisit.append([i+1, j, True])
                    ct[i + 1][j][0] = count + 1
                    ct[i + 1][j][1] = True
        else:
            if ct[i+1][j][0] > count + 1 and arr[i+1][j] == 0:
                tovisit.append([i+1, j, False])
                ct[i+1][j][0] = count + 1
                ct[i+1][j][1] = False


    if j < m-1:
        if breakable:
            if ct[i][j+1][1] == False and arr[i][j+1] == 0:
                tovisit.append([i,j+1,True])
                ct[i][j+1][0] = count+1
                ct[i][j+1][1] = True
            elif arr[i][j+1] == 1:
                if ct[i][j+1][0] > count+1:
                    tovisit.append([i,j+1,False])
                    ct[i][j+1][0] = count+1
                    ct[i][j+1][1] = False
            else:
                if ct[i][j+1][0] > count + 1:
                    tovisit.append([i, j+1, True])
                    ct[i][j+1][0] = count + 1
                    ct[i][j+1][1] = True
        else:
            if ct[i][j+1][0] > count + 1 and arr[i][j+1] == 0:
                    tovisit.append([i, j+1, False])
                    ct[i][j+1][0] = count + 1
                    ct[i][j+1][1] = False

    if i > 0 :
        if breakable:
            if ct[i-1][j][1] == False and arr[i-1][j] == 0:
                tovisit.append([i-1,j,True])
                ct[i-1][j][0] = count+1
                ct[i-1][j][1] = True
            elif arr[i-1][j] == 1:
                if ct[i-1][j][0] > count+1:
                    tovisit.append([i-1,j,False])
                    ct[i-1][j][0] = count+1
                    ct[i-1][j][1] = False
            else:
                if ct[i - 1][j][0] > count + 1:
                    tovisit.append([i-1, j, True])
                    ct[i - 1][j][0] = count + 1
                    ct[i - 1][j][1] = True
        else:
            if ct[i-1][j][0] > count + 1 and arr[i-1][j] == 0:
                    tovisit.append([i-1, j, False])
                    ct[i-1][j][0] = count + 1
                    ct[i-1][j][1] = False

    if j > 0:
        if breakable:
            if ct[i][j-1][1] == False and arr[i][j-1] == 0:
                tovisit.append([i,j-1,True])
                ct[i][j-1][0] = count+1
                ct[i][j-1][1] = True
            elif arr[i][j-1] == 1:
                if ct[i][j-1][0] > count+1:
                    tovisit.append([i,j-1,False])
                    ct[i][j-1][0] = count+1
                    ct[i][j-1][1] = False
            else:
                if ct[i][j-1][0] > count + 1:
                    tovisit.append([i, j-1, True])
                    ct[i][j-1][0] = count + 1
                    ct[i][j-1][1] = True
        else:
            if ct[i][j-1][0] > count + 1 and arr[i][j-1] == 0:
                    tovisit.append([i, j-1, False])
                    ct[i][j-1][0] = count + 1
                    ct[i][j-1][1] = False

if i==n-1 and j == m-1:
    print(count+1)
else:
    print(-1)