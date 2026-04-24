import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

x = input().strip()
if len(x) == 3:
    if x[0:2] == "10":
        print(10+int(x[2:]))
    else:
        print(10+int(x[0]))
elif len(x) ==4:
    print(20)
else:
    print(int(x[0])+int(x[1]))