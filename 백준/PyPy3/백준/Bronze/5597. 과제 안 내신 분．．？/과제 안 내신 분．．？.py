import sys
input= sys.stdin.readline

a = [0] * 30

for i in range (0,28):
    b = int(input())
    a[b-1] = 1

for i in range(0,30):
    if(a[i] == 0):
        print(i+1)
