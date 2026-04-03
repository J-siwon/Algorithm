import sys
import math
from collections import deque, Counter

w,h = map(int, input().split())
r = int(input())
print(w*h - math.pi * r**2/4)