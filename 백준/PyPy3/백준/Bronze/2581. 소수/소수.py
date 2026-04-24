import sys
input= sys.stdin.readline

x = int(input())
y = int(input())
prime = []
for i in range(x, y+1):
    if i == 2:
        prime.append(i)
    for j in range(2,i):
        if (i % j ==0):
            break
        if j == i-1:
            prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))