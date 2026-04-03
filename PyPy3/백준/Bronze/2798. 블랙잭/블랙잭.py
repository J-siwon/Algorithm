import sys
input= sys.stdin.readline

a,b = map(int, input().split())

x = list(map(int, input().split()))

dif = b
minsum = 0
for i in range(0, a-2):
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            sum = x[i] + x[j] + x[k]
            if(sum > b):
                continue
            if(b - sum < dif):
                minsum = sum
                dif = b - sum

print(minsum)
