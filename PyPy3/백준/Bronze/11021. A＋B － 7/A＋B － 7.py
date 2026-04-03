import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
for i in range(x):
    n, m = map(int, input().split())
    print("Case #" + str(i+1) +": ", end= "")
    print(n+m)