import sys
input = sys.stdin.readline

a = int(input())
x= 1
ans = []
while (x**2 <= a):
    ans.append(x**2)
    x+=1

print(len(ans))