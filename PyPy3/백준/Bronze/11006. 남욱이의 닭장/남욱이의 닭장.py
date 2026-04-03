import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

x = int(input())
for i in range(x):
    a,b = map(int, input().split())
    t = 2*b-a
    print(t, b-t)