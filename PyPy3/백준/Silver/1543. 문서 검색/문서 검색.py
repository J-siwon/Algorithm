import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

s = input().strip()
t = input().strip()
count = 0
while(True):
    isdone = False
    start = 0
    arr = (0, 0)
    for i in range(len(s)- len(t)+1):
        if s[i:i+len(t)] == t:
            s = s[i+len(t):]
            isdone = True
            break

    if not isdone:
        break

    count += 1

print(count)