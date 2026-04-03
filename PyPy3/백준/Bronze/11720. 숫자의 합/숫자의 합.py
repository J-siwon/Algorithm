import sys
input= sys.stdin.readline

x = int(input())

y = str(input())

a = [0] * x

sum = 0
for i in range (x):
    sum += int(y[i])

print(sum)
