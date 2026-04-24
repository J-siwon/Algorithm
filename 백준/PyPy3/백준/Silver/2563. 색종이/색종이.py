import sys
input = sys.stdin.readline

x= int(input())
a = [[0] * 100 for i in range(100)]

for i in range(x):
    r,c = map(int, input().split())
    for j in range(r, r+10):
        for k in range(c, c+10):
            a[j][k] += 1

area = 0
for i in range(100):
    for j in range(100):
        if a[i][j] >= 1:
            area += 1

print(area)