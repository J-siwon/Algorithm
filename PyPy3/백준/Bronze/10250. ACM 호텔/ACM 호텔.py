import sys
import math
from collections import deque
input = sys.stdin.readline

x= int(input())
for i in range(x):
    h, w, m = map(int, input().split())
    level = (m % h)
    ho = (m-1)//h+1

    if level == 0:
        level = h
    print(100 *level + ho)