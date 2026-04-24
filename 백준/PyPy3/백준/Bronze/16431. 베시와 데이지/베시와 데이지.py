import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

b1, b2 = map(int,input().split())
d1, d2 = map(int,input().split())
j1, j2 = map(int,input().split())

diagb = min(abs(j1-b1), abs(j2-b2))
if abs(j1-b1)> abs(j2-b2):
    diagb += abs((j1-b1)) -diagb
else:
    diagb += abs((j2-b2)) - diagb

j = abs(j1-d1) + abs(j2-d2)
if diagb > j:
    print("daisy")
elif diagb < j:
    print("bessie")
else:
    print("tie")