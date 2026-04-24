import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
a = deque(map(int, input().split()))
b = deque([i+1 for i in range(x)])
for i in range(x):
    xx = a.popleft()
    print(b.popleft(), end = " ")
    if xx>0:
        xx-=1
        for i in range(xx):
            a.rotate(-1)
            b.rotate(-1)
    else:
        for i in range(abs(xx)):
            a.rotate(1)
            b.rotate(1)