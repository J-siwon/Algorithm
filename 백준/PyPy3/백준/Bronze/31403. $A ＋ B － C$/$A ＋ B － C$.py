import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
y = int(input())
z = int(input())
print(x+y-z)
print(int(str(x)+str(y))-int(str(z)))