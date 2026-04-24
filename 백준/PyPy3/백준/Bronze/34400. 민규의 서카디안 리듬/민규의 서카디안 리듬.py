import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())

for i in range(n):
    x = int(input())%25

    if x >=17:
        print("OFFLINE")
    else:
        print("ONLINE")