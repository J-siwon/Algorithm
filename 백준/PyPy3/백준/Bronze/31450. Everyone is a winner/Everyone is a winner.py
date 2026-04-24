import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
if n % m == 0:
    print("Yes")
else:
    print("No")
