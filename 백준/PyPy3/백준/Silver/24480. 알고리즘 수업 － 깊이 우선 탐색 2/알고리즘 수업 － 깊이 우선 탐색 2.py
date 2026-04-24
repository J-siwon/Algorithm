import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(5*10**5)

def dfs(x):
    global count
    arr[x].sort(reverse = True)
    for i in arr[x]:
        if num[i] != 0:
            continue
        else:
            count += 1
            num[i] = count
            dfs(i)

n,m,r = map(int, input().split())
arr = [[] for i in range(n+1)]
count = 1
num = [0 for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

num[r] = 1
dfs(r)

for i in range(1,n+1):
    print(num[i])