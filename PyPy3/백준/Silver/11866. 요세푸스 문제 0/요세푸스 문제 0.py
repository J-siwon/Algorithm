import sys
from collections import deque
input = sys.stdin.readline

x, y = map(int, input().split())
a = deque([i+1 for i in range(x)])
i = 1
ans = []
b = y
while(len(a)>1):
    times = 0
    c= len(a)
    while(b <= len(a)):
        ans.append(a[b-1])
        times+=1
        b +=y
    for j in range(1,times+1):
        a.remove(ans[-j])
    
    if b != c:
        b = b - c

if(len(a) == 1):
    ans.append(a[0])

print("<", end = "")
for i in range(len(ans)-1):
    print(ans[i], end = ", ")
print(ans[-1], end = ">")
