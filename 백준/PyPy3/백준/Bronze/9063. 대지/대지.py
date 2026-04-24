import sys
input = sys.stdin.readline

x = int(input())

a = []
b = []
for i in range(x):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

print((max(a) - min(a))* (max(b) - min(b)))