import sys
from collections import deque
input = sys.stdin.readline


alpha = "abcdefghijklmnopqrstuvwxyz"
x = int(input())
xx = input().strip()
ans = 0
for i in range(len(xx)):
    for j in range(len(alpha)):
        if xx[i] == alpha[j]:
            ans += 31**(i)*(j+1)
            ans %= 1234567891
print(ans)
