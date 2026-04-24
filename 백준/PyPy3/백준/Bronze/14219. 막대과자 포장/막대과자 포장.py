import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

a,b = map(int,input().split())

if a%3 ==0:
    print("YES")
else:
    if b%3==0:
        print("YES")
    else:
        print("NO")
