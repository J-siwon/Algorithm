import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n,m = map(int, input().split())
arr1 = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    arr1[i] = list(map(int,input().split()))

m,k = map(int, input().split())
arr2 = [[0 for i in range(k)] for i in range(m)]
for i in range(m):
    arr2[i] = list(map(int, input().split()))

arr3 = [[0 for i in range(k)] for i in range(n)]
for i in range(n):
    for j in range(k):
        for q in range(m):
            arr3[i][j] += arr1[i][q] * arr2[q][j]

for i in range(n):
    print(*arr3[i])
