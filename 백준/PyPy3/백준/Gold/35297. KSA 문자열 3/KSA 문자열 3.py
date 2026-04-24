import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

s = input().strip()
goal = ["A", "K", "S"]
c = len(s)
t = len(s)
while t>0:
    if s[t-1] == goal[t%3]:
        c -=1
    else:
        break
    t-=1

temps = list(s[:c])
e = 0
while len(temps) > 0:
    if len(temps) == 2:
        if temps[0] == goal[(c-e-1)%3] and temps[1] == goal[(c-e)%3]:
            e +=2
        break
    p = temps.pop()

    while p == goal[(c-e)%3]:
        e +=1
        if len(temps) > 0:
            p = temps.pop()

    if len(temps) > 0:
        temps.pop()
    else:
        break


print(2*c-2*e)