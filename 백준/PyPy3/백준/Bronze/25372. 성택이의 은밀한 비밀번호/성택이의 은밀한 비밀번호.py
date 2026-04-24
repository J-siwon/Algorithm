import sys
input= sys.stdin.readline


x = int(input())
for i in range(x):
    ans = input().strip()
    if(6<= len(ans) <=9):
        print("yes")
    else:
        print("no")