import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def find(x):
    if x == root[x]:
        return x
    else:
        return find(root[x])
n,m = map(int, input().split())
root = [i for i in range(n)]
arr = [[] for i in range(n) ]
isdone = False
for i in range(m):
    a,b = map(int, input().split())
    if a==b:
        continue
    if a > b:
        (a,b) = (b,a)
    if find(a) == find(b):
        print(i+1)
        isdone = True
        break
    root[find(b)] = find(a)
    arr[a].append(b)

if not isdone:
    print(0)