import sys
input = sys.stdin.readline

times = int(input())
a =set()
count = 0
for i in range(times):
    x = input().strip()
    a.add(x)
    if x == "ENTER":
        count += len(a)- 1
        a = set()
    
count += len(a)
print(count)