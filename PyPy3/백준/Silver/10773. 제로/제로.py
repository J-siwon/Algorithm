import sys
input = sys.stdin.readline

x = int(input())
a = []
for i in range(x):
    xx = int(input())
    if xx == 0:
        a.pop()
    else:
        a.append(xx)

print(sum(a))