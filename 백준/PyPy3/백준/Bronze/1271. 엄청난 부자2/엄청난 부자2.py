import sys
import math
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())
print(a//b)
print(a%b)