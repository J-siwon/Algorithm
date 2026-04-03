import sys
import math
from collections import deque, Counter
# sys.setrecursionlimit(5*10**5)

arr = list(input().split("("))
if len(arr) > 1:
    print(arr[0])
    arr[-1] = arr[-1][:-1]
    print(*arr[1:])
else:
    print(*arr)
    print("-")