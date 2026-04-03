import sys
input= sys.stdin.readline

x = int(input())
if(x > 0):
    a = list(map(int, input().split()))

count = 0
for i in range(x):
    if a[i] == 2:
        count +=1
    for j in range(2, a[i]):
        if a[i] % j == 0:
            break
        if j == a[i]-1:
            count += 1

print(count)