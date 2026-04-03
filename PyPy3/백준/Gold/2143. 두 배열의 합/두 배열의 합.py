import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

t = int(input())
alen = int(input())
arr1 = list(map(int, input().split()))
blen = int(input())
arr2 = list(map(int, input().split()))

dp1 = [0 for i in range(alen+1)]
dp2 = [0 for i in range(blen+1)]
for i in range(1,alen+1):
    dp1[i] = dp1[i-1] +arr1[i-1]

for i in range(1, blen + 1):
    dp2[i] = dp2[i - 1] + arr2[i - 1]

sarr1 = []
for i in range(len(dp1)):
    for j in range(i+1,len(dp1)):
        sarr1.append(dp1[j]- dp1[i])

sarr2 = []
for i in range(len(dp2)):
    for j in range(i+1,len(dp2)):
        sarr2.append(dp2[j]- dp2[i])

sarr1.sort()
sarr2.sort()
count = 0
c = Counter(sarr2)
for i in sarr1:
    target = t-i

    low = 0
    high = len(sarr2)-1
    while(low<high):
        mid = (low+high)//2
        if sarr2[mid] >= target:
            high = mid
        else:
            low = mid +1

    if sarr2[low] == target:
        count += c[sarr2[low]]
print(count)