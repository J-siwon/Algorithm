import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
a = list(input().split())
b = list(input().split())

s1 = ""
s2 = ""
for i in a:
    s1 += i

for i in b:
    s2 += i

if int(s1) > int(s2):
    print(s2)
else:
    print(s1)