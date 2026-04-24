import sys
input= sys.stdin.readline

a = [0] * 10

for i in range(0,10):
    x = int(input())
    a[i] = x % 42


count = 0
for j in range(0,42):
    for i in range(0,10):
        if(a[i] == j):
            count += 1
            break

print(count)
