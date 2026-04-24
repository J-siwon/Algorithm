import sys
import math
from collections import deque, Counter
# sys.setrecursionlimit(5*10**5)

def recur(t):
    global count
    global isdone
    if t > b:
        count -=1
        return
    t1 = t*2
    t2 = 10*t+1
    if t1 == b or t2 == b:
        print(count+1)
        isdone = True
        return

    count +=1
    recur(t1)
    count +=1
    recur(t2)
    count -=1

a,b = map(int, input().split())

t = a
count = 1
isdone = False
recur(t)

if not isdone:
    print(-1)
