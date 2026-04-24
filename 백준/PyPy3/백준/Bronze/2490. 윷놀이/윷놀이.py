import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

for i in range(3):
    arr = list(map(int,input().split()))
    s = Counter(arr)[0]
    if s ==0:
        print("E")
    elif s==1:
        print("A")
    elif s==2:
        print("B")
    elif s==3:
        print("C")
    elif s==4:
        print("D")