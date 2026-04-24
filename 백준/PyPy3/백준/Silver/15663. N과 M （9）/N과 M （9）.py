import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(5*10**5)

def nmp(x, arr):
    global n,m
    global visited
    global last
    if len(x) == m:
        if x == visited:
            return
        else:
            print(*x)
            visited = x.copy()
            return
    last = -1
    for i in range(len(arr)):
        t = arr.pop(i)
        if last == t:
            arr.insert(i,t)
            continue
        x.append(t)
        nmp(x,arr)
        arr.insert(i, t)
        x.pop()
        last = t


n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
last = 0
visited = []

nmp([],arr)