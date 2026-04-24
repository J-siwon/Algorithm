import sys
input = sys.stdin.readline

a = [0] * 10000
n, k = map(int, input().split())
index = 0
for i in range(1, n+1):
    if(n % i == 0):
        a[index] += i
        index += 1
        

if(len(a) < k):
    print(0)
else:
    print(a[k-1])