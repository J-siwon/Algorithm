import sys
input = sys.stdin.readline

a = [0] * 9
max = 0
maxindex = 0
for i in range(0, 9):
    a[i] = int(input())
    if(a[i] > max):
        max = a[i]
        maxindex = i+1

print(max)
print(maxindex)