import sys
input = sys.stdin.readline

n, m = map(int, input().split())

x = [0] * n
a = ""
for r in range(0,m):
    i, j, k = map(int, input().split())
    for c in range(i-1, j):
        x[c] = k

for r in range(0, n):
    a += str(x[r])
    a += " "

print(a)