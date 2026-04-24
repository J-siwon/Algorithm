import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
t = math.floor(x* 0.15+0.5)

arr = deque()
for i in range(1,x+1):
    r = int(input())
    arr.append(r)

arr = deque(sorted(arr))

for _ in range(t):
    arr.pop()
    arr.popleft()

if x > 0:
    print(math.floor(sum(arr) / len(arr)+0.5) )
else:
    print(0)