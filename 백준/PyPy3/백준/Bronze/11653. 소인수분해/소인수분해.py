import sys
input= sys.stdin.readline

x = int(input())
for i in range(2, x+1):
    if x % i != 0:
        continue
    if x==1:
        break
    while x % 2 == 0:
        x = x//2
        print(2)
        if x == 1:
            break
    for j in range(2,i):
        if (i % j ==0):
            break
        if j == i-1:
            while x % i == 0:
                x = x//i
                print(i)
                if x == 1:
                    break