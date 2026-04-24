import sys
input = sys.stdin.readline

a = [[0] * 9 for j in range(9)]

for i in range(9):
    a[i] = list(map(int, input().split()))

max = 0
maxi = 0
maxj = 0
for i in range(1, 10):
    for j in range(1, 10):
        if(max <= a[i-1][j-1]):
            max = a[i-1][j-1]
            maxi = i
            maxj = j


print(max)
print(str(maxi) + " " + str(maxj))