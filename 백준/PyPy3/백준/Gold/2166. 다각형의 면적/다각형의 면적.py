import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    a,b = map(int, input().split())
    arr.append((a,b))

arr.append(arr[0])
t = 0
for i in range(1,len(arr)):
    t += arr[i-1][0] * arr[i][1] - arr[i][0] * arr[i-1][1]

print(abs(t)/2)