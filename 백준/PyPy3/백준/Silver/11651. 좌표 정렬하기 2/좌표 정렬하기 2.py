import sys
input = sys.stdin.readline

x = int(input())
a = []
for i in range(x):
    a.append(list(map(int, input().split())))

a = sorted(a, key= lambda x: x[0])
a = sorted(a, key= lambda x: x[1])
for i in range(len(a)):
    print(*a[i])