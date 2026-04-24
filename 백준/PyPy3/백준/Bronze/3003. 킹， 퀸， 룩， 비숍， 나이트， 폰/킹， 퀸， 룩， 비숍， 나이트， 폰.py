import sys
input= sys.stdin.readline

x = [1,1,2,2,2,8]

a = list(input().split())

for i in range(len(a)):
    a[i] = x[i] - int(a[i])

print(*a)
