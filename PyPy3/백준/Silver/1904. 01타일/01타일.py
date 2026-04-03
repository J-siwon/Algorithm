import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
temp2 = 1
temp = 1
ans = 2
for i in range(2,x):
    temp2 = temp
    temp = ans
    ans += temp2
    if ans > 15746:
        temp2%= 15746
        temp %= 15746
        ans %= 15746
if x == 1:
    ans = 1
print(ans % 15746)