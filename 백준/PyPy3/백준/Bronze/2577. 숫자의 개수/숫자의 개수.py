import sys
import math
from collections import deque
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

mul = a * b*c
lst = [0,0,0,0,0,0,0,0,0,0]
for i in str(mul):
    lst[int(i)]+= 1

for i in range(10):
    print(lst[i])