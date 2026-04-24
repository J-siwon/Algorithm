import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

arr = 0
x = int(input())
s = input().strip()
t = 0
b = False
double = False
for i in s:
    if i == 'P':
        if arr == 0:
            b = b == False
        if arr==1:
            double = True
    else:
        if arr == 0 :
            arr+=1
        elif arr==1:
            arr +=1
        else:
            break

if arr>=2:
    if double:
        t+=6
    else:
        if b == True:
            t+=1
        else:
            t+=5
print(t)
