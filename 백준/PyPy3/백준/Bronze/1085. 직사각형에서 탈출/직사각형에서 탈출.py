import sys
input = sys.stdin.readline

a,b,c,d = map(int, input().split())

min = 0

if 0<= a <=c :
    if(a-0) < (c-a):
        min = a
    else:
        min = c-a
else:
    min = a-c

if 0<= b <= d:
    if(b-0) < (d-b):
        if min > b-0:
            min = b-0
    else:
        if min > d-b:
            min = d-b
else:
    if b-d < min:
        min = b-d 

print(min)