import sys
input = sys.stdin.readline

r, c = map(int, input().split())

a = [[0] * c for j in range(r)]
b = [[0] * c for j in range(r)]


for i in range(r):
    x = list(map(int, input().split()))
    for j in range(c):
        a[i][j] = x[j]

for i in range(r):
    x = list(map(int, input().split()))
    for j in range(c):
        b[i][j] = x[j]

for i in range(r):
    for j in range(c):
        a[i][j] += b[i][j]
    
    print(*a[i])
