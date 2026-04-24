import sys
import math
from collections import deque
input = sys.stdin.readline

while(True):
    try:
        x,y = map(int, input().split())
        print(x+y)
    except:
        break