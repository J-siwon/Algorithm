import sys
input = sys.stdin.readline

x= int(input())
for i in range(x):
    a,b = map(int, input().split())
    maxq = 1
    for i in range(1,min(a,b)+1):
        if a % i ==0 and b %i == 0:
            maxq =i
    
    print(b * (a // maxq))