import sys
input= sys.stdin.readline

a= [0] * 36
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(36):
    a[i] = i

n10, b = map(int, input().split())
rem = n10
temp = ""

i=1
q =1
while(q >0):
    q = rem // (b ** i)
    i += 1

i-= 2
while(i >= 0):
    q = rem // (b ** i)
    temp += alpha[q]
    rem = rem % (b ** i)
    i -= 1

print(temp)