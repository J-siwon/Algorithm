import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

l = int(input())
s = input().strip()
d,m = map(int, input().split())

t = "HYU"
index = -1
num = 0
dcount = 0
mcount = 0
e = 0
for i in s:
    if i in t:
        if mcount ==0:
            continue
        elif mcount ==1:
            e+=d
            mcount =0
        else:
            e+=min(m+d, mcount*d)
            mcount = 0
    else:
        mcount+=1    

if mcount ==1:
    e+=d
    mcount =0
elif mcount >1:
    e+=min(m+d, mcount*d)
    mcount = 0

if e ==0:
    print("Nalmeok")
else:
    print(e)

index = 2
c = Counter(s)
t = min(c["H"], c["Y"], c["U"])
if t ==0:
    print("I love HanYang University")
else:
    print(t)