import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(2*10**5)

n,m,s = map(int, input().split())
arr = [[[] for i in range(m)]for i in range(s)]

for i in range(s):
    for j in range(m):
        arr[i][j] = list(map(int, input().split()))

tovisit = deque()
count = 1
for p in range(s):
    for q in range(m):
        for r in range(n):
            if arr[p][q][r] == 1:
                if p>0:
                    if arr[p - 1][q][r] == 0:
                        arr[p-1][q][r] = 2
                        tovisit.appendleft([p - 1, q,r, count])
                if q > 0:
                    if arr[p][q - 1][r] == 0:
                        arr[p][q-1][r] = 2
                        tovisit.appendleft([p, q - 1,r, count])
                if p < s - 1:
                    if arr[p + 1][q][r] == 0:
                        arr[p+1][q][r] = 2
                        tovisit.appendleft([p + 1, q,r, count])
                if q < m - 1:
                    if arr[p][q + 1][r] == 0:
                        arr[p][q+1][r] = 2
                        tovisit.appendleft([p, q + 1,r, count])
                if r > 0:
                    if arr[p][q][r-1] == 0:
                        arr[p][q][r-1] = 2
                        tovisit.appendleft([p, q,r-1, count])
                if r < n-1:
                    if arr[p][q][r+1] == 0:
                        arr[p][q][r+1] = 2
                        tovisit.appendleft([p, q, r + 1, count])

lastcount = 0
isdone = False
while(len(tovisit) > 0):
    t = tovisit.pop()
    p = t[0]
    q = t[1]
    r = t[2]
    count = t[3] +1

    arr[p][q][r] = 1
    if p > 0:
        if arr[p - 1][q][r] == 0:
            arr[p - 1][q][r] = 2
            tovisit.appendleft([p - 1, q, r, count])
    if q > 0:
        if arr[p][q - 1][r] == 0:
            arr[p][q - 1][r] = 2
            tovisit.appendleft([p, q - 1, r, count])
    if p < s - 1:
        if arr[p + 1][q][r] == 0:
            arr[p + 1][q][r] = 2
            tovisit.appendleft([p + 1, q, r, count])
    if q < m - 1:
        if arr[p][q + 1][r] == 0:
            arr[p][q + 1][r] = 2
            tovisit.appendleft([p, q + 1, r, count])
    if r > 0:
        if arr[p][q][r - 1] == 0:
            arr[p][q][r - 1] = 2
            tovisit.appendleft([p, q, r - 1, count])
    if r < n - 1:
        if arr[p][q][r + 1] == 0:
            arr[p][q][r + 1] = 2
            tovisit.appendleft([p, q, r + 1, count])



isdone = False
for i in range(s):
    for j in range(m):
        if 0 in arr[i][j]:
            print(-1)
            isdone = True
            break
    if isdone:
        break

if not isdone:
    print(count-1)