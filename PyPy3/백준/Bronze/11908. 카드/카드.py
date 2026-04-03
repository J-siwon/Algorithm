n = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
print(sum(arr)- arr[-1])