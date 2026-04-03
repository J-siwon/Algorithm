import sys
input = sys.stdin.readline

x = int(input())
a =[]
for i in range(x):
    a.append(input().split())
    a[i] = (a[i], i)

a = sorted(a, key= lambda x: (int(x[0][0]), x[1]))

for i in range(len(a)):
    print(*a[i][0])