import sys
input= sys.stdin.readline

x = int(input())
q = 0
r = 0

for i in range(x):
    a = 0
    r = i
    for j in range(1, len(str(i))):
        q = r // 10 ** (len(str(i))-j)
        r = i % (10 ** (len(str(i))-j))
        if(q>0):
            a += q
    a += r
    a += i
    if(a == x):
        print(i)
        break

    if(i == x-1):
        print(0)