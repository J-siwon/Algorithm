import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def CheckDone():
    global is1
    is1 = False
    for j in done:
        l = len(j)
        for k in range(0, len(dp)):
            if k - l >= 0 and dp[k - l] == 1:
                if "".join(arr[k - l + 1:k + 1]) == j:
                    if dp[k]==0:
                        dp[k] = 1
                        is1 = True

a = input().strip()
n = int(input())
inputlist = []
dp = [0 for i in range(len(a))]
for i in range(n):
    inputlist.append(input().strip())

inputlist = sorted(inputlist, key = lambda x: len(x), reverse= True)

done = []
arr = list(a)

for i in range(len(inputlist)):
    is1 = True
    x = inputlist.pop()
    while(is1):
        is1 = False
        l = len(x)
        if l == 0:
            break
        if x == "".join(arr[0:l]):
            if dp[l-1] == 0:
                dp[l-1] = 1
                is1 = True

        for j in range(0,len(dp)):
            if j-l >= 0 and dp[j-l]== 1:
                if "".join(arr[j-l+1:j+1]) == x:
                    if dp[j]==0:
                        dp[j] = 1
                        is1 = True

        while is1:
            CheckDone()


    done.append(x)

print(dp[-1])