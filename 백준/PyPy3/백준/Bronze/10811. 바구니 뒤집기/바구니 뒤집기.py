import sys
input= sys.stdin.readline

x, y = map(int, input().split())

a = [0] * x
for i in range(0,x):
    a[i] = i+1

for k in range(0,y):
    i, j = map(int, input().split())
    t = 0
    while(i+t< (i+j)/2):
        temp = a[i-1+t]
        a[i-1+t] = a[j-1-t]
        a[j-t-1] = temp
        t += 1

pr = ""
for i in range(0,x):
    pr = pr + str(a[i]) + " "

print(pr)
