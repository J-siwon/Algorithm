import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

t = list(map(int, input().split()))
count = 0
while len(t) != 1:
    count +=1
    if (t[1]**2 + t[2]**2)**(1/2) > 2* t[0]:
        print("Pizza " + str(count) + " does not fit on the table.")
    else:
        print("Pizza " + str(count) + " fits on the table.")
    t = list(map(int, input().split()))