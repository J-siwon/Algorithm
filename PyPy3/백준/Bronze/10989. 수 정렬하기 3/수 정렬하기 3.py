import sys
input = sys.stdin.readline

a = [0] * 10000
x = int(input())
for j in range(x):
    q = int(input())
    a[q-1] += 1

for i in range(10000):
    for j in range(a[i]):
        print(i+1)