import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
a = sorted(a)
while (a[0] + a[1] <= a[2]):
    a[2] -= 1
print(sum(a))