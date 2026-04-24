import sys
import math
from collections import deque, Counter

a,b = map(int, input().split())
t = []
for i in range(a):
    *arr, name = input().split()
    count = 0
    maxcount = 0
    for j in arr:
        if j == '*':
            if count >0:
                maxcount = max(maxcount, count)
            count = 0
        else:
            count +=1
    maxcount = max(maxcount, count)
    t.append([maxcount, name])

s = set()
for i in t:
    s.add(i[0])
print(len(s))
for i in t:
    print(*i)