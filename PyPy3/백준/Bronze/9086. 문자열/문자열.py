import sys
import math
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    x = input().strip()
    print(x[0], end="")
    print(x[-1])