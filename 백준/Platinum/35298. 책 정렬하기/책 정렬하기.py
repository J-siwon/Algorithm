import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
target = n
ans = []

while target > 2:
    tarr = []
    ind = arr.index(target) +1 #가장 높은 수의 번지수

    if (target - ind) % 2 == 0: #target 뒤가 짝수개
        for i in range(ind, target): #target 뒤를 tarr에 추가
            tarr.append(arr[i])
            if i%2 == 1: #뒤에서 2번째를 앞으로 넘기는 방식을 반복
                ans.append(target-1)

        for i in range(ind-1): #target 앞쪽을 tarr에 추가 (target 제외)
            tarr.append(arr[i])

    else: #target 뒤가 홀수개
        if target % 2 == 0: # 현재 arr의 길이가 짝수개 (ex : 2 1 4 3)
            if ind == 1:
                ans.append(3)
                (arr[0], arr[2]) = (arr[2], arr[0])
                (arr[1], arr[3]) = (arr[3], arr[1])
                continue

            tarr.append(arr[ind-2]) #가장 높은 수 이전것을 tarr 추가 (ex : 1)
            tarr.append(target) #가장 높은 수를 추가 tarr (ex : 4)

            for i in range(ind-2): # 가장 높은 수 전 수보다 전에 있는 tarr에 추가(ex : 2)
                tarr.append(arr[i])

            for i in range(ind, target): # 가장 높은 수 다음 수부터 tarr (ex: 3)
                tarr.append(arr[i])

            arr = tarr.copy()
            ans.append(ind-1)
            continue #재실행
        else: # 현재 arr의 길이가 홀수개 (ex : 2 1 4 5 3)
            tarr.append(target) #가장 높은수 (5)
            tarr.append(arr[ind]) #가장 높은 수 다음 수 (3)

            for i in range(ind-1): #이전 수 (ex: 2 1 4)
                tarr.append(arr[i])

            for i in range(ind+1, target): # 이후 수 (ex : X)
                tarr.append(arr[i])

            arr = tarr.copy()
            ans.append(ind)
            continue #재실행

    arr = tarr.copy()
    target -= 1

if arr == [2,1]:
    print("NO")
else:
    print("YES")
    print(len(ans))
    print(*ans)