import sys
import math
from collections import deque, Counter
input = sys.stdin.readline
sys.setrecursionlimit(2*10**5)

def dfs(x):
    for i in inputlist[x]:
        if x in inputlist[i]:
            inputlist[i].remove(x)
        arr[i] = x
        dfs(i)

n = int(input())
arr = [-1 for i in range(n+1)]
inputlist = [[] for i in range(n+1)]

for i in range(n-1):
    a,b = map(int, input().split())
    inputlist[a].append(b)
    inputlist[b].append(a) 

dfs(1)

for i in range(2,len(arr)):
    print(arr[i])