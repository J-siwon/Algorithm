import sys
input = sys.stdin.readline

x = int(input())
a = []
for i in range(x):
    x = int(input())
    a.append(x)
a = sorted(a)
for i in range(len(a)):
    print(a[i])
