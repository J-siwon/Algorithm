import sys
input = sys.stdin.readline

x = 5
a = []
for i in range(x):
    x = int(input())
    a.append(x)
a = sorted(a)
print(sum(a) // len(a))
print(a[2])