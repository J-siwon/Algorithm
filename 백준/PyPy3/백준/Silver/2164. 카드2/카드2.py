import sys
import math
input = sys.stdin.readline

x = int(input())

a = []
for i in range(1,x+1):
    a.append(i)

while len(a) > 3:
    b = []
    if (len(a)) % 2 == 0:
        for i in range(1,len(a)//2+1):
            b.append(a[2*i-1])    
    else:
        for i in range(2, len(a)//2+1):
            b.append(a[2*i-1])
        b.append(a[1])
    a = b


if len(a) == 3 or len(a) == 2:
    print(a[1])
else:
    print(a[0])
