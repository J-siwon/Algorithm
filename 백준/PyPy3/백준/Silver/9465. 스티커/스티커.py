import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())

for i in range(n):
    x= int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    dp1 = [0 for j in range(x)]
    dp2 = [0 for j in range(x)]
    dp1[0] = arr1[0]
    dp2[0] = arr2[0]
    if x>1:
        dp1[1] = arr2[0] + arr1[1]
        dp2[1] = arr1[0] + arr2[1]

    for j in range(2,x):
        dp1[j] = max(dp2[j-2] + arr1[j], dp2[j-1] + arr1[j])
        dp2[j] = max(dp1[j-1], dp1[j-2]) +arr2[j]

    print(max(dp1[x-1], dp2[x-1]))