import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

at, a = map(int,input().split())
bt, b = map(int,input().split())
ct, c = map(int,input().split())
hp = int(input())
hp = hp-a-b-c
times =0
x =at
y = bt
z =ct
while(hp>0):
    if x == 1:
        hp-=a
        x = at
    else:
        x -=1
    if y == 1:
        hp -= b
        y = bt
    else:
        y -= 1
    if z == 1:
        hp-=c
        z = ct
    else:
        z -=1
    times+=1
print(times)