import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] == x:
        return parent[x]
    else:
        parent[x] = find(parent[x])
        return parent[x]

n,m = map(int, input().split())

parent = [i for i in range(n+1)]
q = []
for i in range(m):
    a,b,c = map(int, input().split())
    q.append((a,b,c))

q.sort(key= lambda x : x[2])
cost = 0
for t in q:
    a = find(t[0])
    b= find(t[1])
    if a == b:
        continue

    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    cost += t[2]

print(cost)