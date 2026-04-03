import sys
input = sys.stdin.readline

x = int(input())
a = []
for i in range(x):
    a.append(list(map(int, input().split())))

a = sorted(a)
for i in range(len(a)):
    print(*a[i])