import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

x= int(input())

if x>2**15-1 or x<-2**15:
    if x>2**31-1 or x<-2**31:
        print("long long")
    else:
        print("int")
else:
    print("short")