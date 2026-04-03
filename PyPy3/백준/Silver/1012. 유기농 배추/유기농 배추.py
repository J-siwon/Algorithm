import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(5*10**5)

def visit(i,j,visited):
    global count
    if i>=r or i<0 or j>=c or j<0:
        return
    if [i,j] in visited or mp[i][j] == 0:
        return
    else:
        visited.append([i,j])

    visit(i-1,j,visited)
    visit(i+1,j,visited)
    visit(i,j-1,visited)
    visit(i,j+1,visited)


n = int(input())
mp = []
for q in range(n):
    r, c, k = map(int, input().split())
    mp = [[0 for i in range(c)] for i in range(r)]

    for i in range(k):
        a,b = map(int, input().split())
        mp[a][b] = 1

    count = 0

    visited = []
    for i in range(0,r):
        for j in range(0,c):
            if mp[i][j] == 1:
                if [i,j] not in visited:
                    visit(i,j,visited)
                    count+=1

    print(count)