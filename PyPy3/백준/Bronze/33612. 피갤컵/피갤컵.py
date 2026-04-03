import sys
import math
from collections import deque
input = sys.stdin.readline

x= int(input())

print(2024 + (x*7)//12, end=" ")
t=(x*7+1)
if t%12==0 :
    print(12)
else:
    print(t%12)