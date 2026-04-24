import sys
input = sys.stdin.readline

a, b = map(int, input().split())
while(a<=b):
    isprime = True
    if(a <= 2):
        a = 2
    for j in range(2, int(a**(1/2))+1):
        if a % j == 0:
            isprime = False
            break
    if isprime:
        print(a)
    a+=1