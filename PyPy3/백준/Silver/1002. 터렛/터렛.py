import sys
import math
from collections import deque, Counter
n = int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    if d > r1+r2:
        print(0)
    elif d == r1+r2:
        print(1)
    else:
        if x1 == x2 and y1 == y2 and r1 == r2:
            print(-1)
        elif max(r1,r2) > min(r1,r2) + d:
            print(0)
        elif max(r1,r2) == min(r1,r2) + d:
            print(1)
        else:
            print(2)