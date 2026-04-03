import sys
input = sys.stdin.readline

a = []
for i in range(2):
    a.append(list(map(int, input().split())))

q = []
for i in range(2,max(a[0][1], a[1][1])+1):
    if a[0][1] % i ==0 or a[1][1] %i == 0:
        q.append(i)

x = [a[0][0] * a[1][1] + a[1][0] * a[0][1] , a[1][1] * a[0][1]]

for i in q:
    while(x[0] % i ==0 and x[1] % i == 0):
        x[0] = x[0] //i
        x[1] = x[1] //i
print(*x)