import sys
input= sys.stdin.readline

a= [0] * 36
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(10):
    a[i] = i
for i in range(10, 36):
    a[i] = i

n, b = input().split()

n10 = 0
temp = [0] * len(n)
for i in range(len(n)):
    for j in range(36):
        if(alpha[j] == n[i]):
            temp[i] = a[j]

for i in range(len(n)):
    n10 += temp[len(n) - i-1] * int(b) ** i

print(n10)