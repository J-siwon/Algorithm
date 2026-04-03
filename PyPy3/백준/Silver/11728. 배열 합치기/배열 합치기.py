n,m = map(int, input().split())
arr = []
for i in list(map(int, input().split())):
    arr.append(i)
    
for i in list(map(int, input().split())):
    arr.append(i)

arr.sort()
print(*arr)