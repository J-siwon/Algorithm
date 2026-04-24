import sys
input= sys.stdin.readline

x = input()
y = "abcdefghijklmnopqrstuvwxyz"

a = [-1]* 26
for i in range(len(y)):
    for j in range(len(x)):
        if(y[i] == x[j]):
            a[i] = j
            break
            

print(*a)
