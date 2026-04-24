import sys
input = sys.stdin.readline

n, m = map(int, input().split())

x = [0] * n
for i in range(1, n+1):
    x[i-1] = i


for j in range(0, m):
    a, b = map(int, input().split())
    temp = x[a-1]
    x[a-1] = x[b-1]
    x[b-1] = temp

a = ""
for k in range(0,n):
    a = a + str(x[k]) + " "

print(a)