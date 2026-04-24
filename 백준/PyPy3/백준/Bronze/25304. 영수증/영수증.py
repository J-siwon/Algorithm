import sys
input = sys.stdin.readline

x = int(input())
y = int(input())
count = 0

for i in range(1, y+1):
    a, b = map(int, input().split())
    count += a * b

if(x == count):
    print ("Yes")
else:
    print("No")