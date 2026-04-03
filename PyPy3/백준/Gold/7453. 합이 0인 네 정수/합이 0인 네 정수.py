import heapq
import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
a = []
b = []
c = []
d = []

for i in range(n):
    x,y,z,w = map(int, input().split())
    a.append(x)
    b.append(y)
    c.append(z)
    d.append(w)


arr1 = []
arr2 = []
for i in range(n):
    for j in range(n):
        arr1.append(a[i] + b[j])
        arr2.append(c[i] + d[j])

c2 = dict()
for i in range(len(arr2)):
    if arr2[i] in c2:
        c2[arr2[i]] += 1
    else:
        c2[arr2[i]] = 1

count = 0
for i in range(len(arr1)):
    t = -arr1[i]

    if t in c2:
        count += c2[t]

print(count)