import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
for i in range(x):
    for j in range(x-i-1,x):
        print("*", end="")
    print()