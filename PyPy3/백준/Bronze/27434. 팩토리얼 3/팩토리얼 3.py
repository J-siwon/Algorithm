import sys
input= sys.stdin.readline


x = int(input())
ans = 1
for i in range(1,x+1):
    ans *= i
print(ans)