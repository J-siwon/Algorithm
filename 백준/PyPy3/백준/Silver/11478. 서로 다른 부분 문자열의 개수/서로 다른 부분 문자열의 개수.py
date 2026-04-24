import sys
input = sys.stdin.readline

x= input().strip()
a = []
for i in range(1,len(x)+1):
    for j in range(len(x)-i+1):
        a.append(x[j:j+i])
print(len(set(a)))