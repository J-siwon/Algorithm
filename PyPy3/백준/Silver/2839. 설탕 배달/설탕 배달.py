import sys
input = sys.stdin.readline

x = int(input())

max5 = 0

for i in range(x//5+1):
    if (x-5*i) % 3 ==0:
        max5= i

x = x - 5 * max5

if x%3 == 0:
    print(x // 3 + max5)
else:
    print(-1)