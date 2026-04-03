import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = 2
l = int(input())
r = int(input())

t = 0
l = (l * r) //100
while(l>5):
    t += n*l
    l = (l * r) //100
    n *=2
print(t)