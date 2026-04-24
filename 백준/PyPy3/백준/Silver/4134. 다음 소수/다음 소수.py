import sys
input = sys.stdin.readline

x = int(input())

for i in range(x):
    a = int(input())
    while(True):
        isprime = True
        if(a <= 2):
            a = 2
            break
        for j in range(2, int(a**(1/2))+2):
            if a % j == 0:
                isprime = False
                break
        if isprime:
            break
        a+=1
    print(a)
