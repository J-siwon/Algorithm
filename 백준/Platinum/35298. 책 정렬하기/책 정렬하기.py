import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

#def move()

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = n
    ans = []

    while target > 1:
        tarr = []
        ind = arr.index(target) +1

        if (target - ind) % 2 == 0:
            for i in range(ind, target):
                tarr.append(arr[i])
                if i%2 == 1:
                    ans.append(i+1)

            for i in range(ind-1):
                tarr.append(arr[i])
        else:
            if target % 2 == 0:
                print("NO")
                return

            tarr.append(target)
            tarr.append(arr[ind])

            for i in range(ind-1):
                tarr.append(arr[i])

            for i in range(ind+1, target):
                tarr.append(arr[i])

            arr = tarr.copy()
            ans.append(ind)
            continue

        arr = tarr.copy()
        target -= 1

    print("YES")
    print(len(ans))
    print(*ans)


main()