import sys
input = sys.stdin.readline

arr = []
for i in range(4):
    arr.append(int(input()))

if sum(arr) + 300 <= 1800:
    print("Yes")
else:
    print("No")