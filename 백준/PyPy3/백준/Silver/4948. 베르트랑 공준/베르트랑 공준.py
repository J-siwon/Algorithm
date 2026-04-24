import sys
input = sys.stdin.readline

a = int(input())
while(a != 0):
    count = 0
    n = a
    a += 1
    while(a<=2 * n):
        isprime = True
        if(a <= 2):
            a = 2
        for j in range(2, int(a**(1/2))+1):
            if a % j == 0:
                isprime = False
                break
        if isprime:
            count+=1
        a+=1
    
    
    print(count)
    a = int(input())

