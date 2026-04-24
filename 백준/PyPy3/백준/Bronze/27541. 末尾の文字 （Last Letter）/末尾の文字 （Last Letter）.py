import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

i = int(input())
x = input().strip()
if x[-1] == "G":
    print(x[:-1])
else:
    print(x + "G")