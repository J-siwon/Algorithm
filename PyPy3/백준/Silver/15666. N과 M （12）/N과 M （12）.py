import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(5*10**5)

def nmp(x, arr):
    global n,m
    global visited
    global last
    global lastlyprinted
    if len(x) == m:
        if x == visited:
            return
        else:
            print(*x)
            visited = x.copy()
            return

    lastlyprinted = []
    for i in range(len(arr)):
        t = arr[i]
        if t < last:
            continue
        last = t
        x.append(t)
        if x == lastlyprinted:
            x.pop()
            continue
        nmp(x,arr)
        lastlyprinted = x.copy()
        x.pop()
        if len(x) >0:
            last = x[-1]
        else:
            last = arr[i]


n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
last = 0
lastlyprinted = []
visited = []

nmp([],arr)