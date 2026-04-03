import sys
input= sys.stdin.readline

x = int(input())
a = [0] * x
b = [0] * x

a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(x):
    if a[i] <= b[i]:
        count+=1

print(count)