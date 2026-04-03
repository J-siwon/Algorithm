import sys
input = sys.stdin.readline

a = int(input())
prime = [i for i in range(1,1000001)]
prime[0] = 0
for i in range(1,1000001):
    if prime[i-1] == 0:
        continue
    times = i
    i += times
    while(i < 1000000):
        prime[i-1] = 0
        i += times

prime = set(prime)
for i in range(a):
    b = int(input())
    count = 0
    for j in range(2,b//2+1):
        if j in prime and b-j in prime:
            count +=1
    print(count)