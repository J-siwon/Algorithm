import sys
import math
from collections import deque, Counter

def Virus(x):
    if vir[x] == 1:
        return
    else:
        vir[x] = 1

    for i in arr[x]:
        Virus(i)

v = int(input())
e = int(input())
arr = [[] for i in range(v+1)]
vir = [0 for _ in range(v+1)]
for i in range(e):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

Virus(1)
print(Counter(vir)[1]-1)
