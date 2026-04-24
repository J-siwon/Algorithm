import sys
import math
from collections import deque
input = sys.stdin.readline

count = 0
for i in range(1, int(input())+1):
    count += i
print(count)