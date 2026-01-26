
n = int(input())
arr = list(map(int,input().split()))
ans = set()
for i in range(1,max(arr)+1):
    x = i
    for j in arr:
        if j%i != 0:
            x = 1
            break
    ans.add(x)
for i in ans:
    print(i)