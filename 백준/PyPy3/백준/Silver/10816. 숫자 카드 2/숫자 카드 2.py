import sys
input = sys.stdin.readline

x = int(input())
arr = list(map(int, input().split()))
dic = dict()
for i in range(len(arr)):
    if arr[i] in dic.keys():
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1

y = int(input())
arr2 = list(map(int, input().split()))

for i in range(len(arr2)):
    if arr2[i] in dic.keys():
        print(dic[arr2[i]], end = " ")
    else:
        print(0, end = " ")
