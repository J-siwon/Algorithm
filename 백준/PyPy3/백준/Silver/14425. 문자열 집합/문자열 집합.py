import sys
input = sys.stdin.readline

x, y = map(int, input().split())
arr = set()
count = 0
for i in range(x):
    arr.add(input().strip())

for j in range(y):
    if input().strip() in arr:
        count+=1

print(count)