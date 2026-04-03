n = int(input())
c = 0
for i in range(1,n+1):
    arr = list(str(i))
    for j in range(len(arr)):
        arr[j] = int(arr[j])
    t = sum(arr)
    if i % t == 0:
        c += 1
        
print(c)