import sys
input = sys.stdin.readline

x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

a = [0] * 2
if x[0] == x[1]:
    a[0] += x[2]
elif x[1] == x[2]:
    a[0] += x[0]
else:
    a[0] += x[1]
a += " "
if y[0] == y[1]:
    a[1] += y[2]
elif y[1] == y[2]:
    a[1] += y[0]
else:
    a[1] += y[1]
    
print(*a)