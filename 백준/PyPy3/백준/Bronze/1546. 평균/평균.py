import sys
input= sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))

max = 0
for i in range(0,n):
    if(max < a[i]):
        max = a[i]

sum = 0
for i in range(0,n):
    a[i] = a[i]/max * 100
    sum += a[i]

print(sum / n)
