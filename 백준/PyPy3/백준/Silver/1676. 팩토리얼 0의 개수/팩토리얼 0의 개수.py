import sys
import math
input = sys.stdin.readline

x = int(input())
a = 1
for i in range(1,x+1):
    a*=i
a = str(a)
count = 0
for i in range(len(a)-1,-1, -1):
    if a[i] != "0":
        break
    count+=1
print(count)