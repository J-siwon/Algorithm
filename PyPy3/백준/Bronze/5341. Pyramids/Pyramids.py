import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

x= int(input())

while(x != 0):
    print(int(x* (x+1) /2))
    x = int(input())