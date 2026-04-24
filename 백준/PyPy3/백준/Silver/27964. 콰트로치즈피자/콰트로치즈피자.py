import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = set()
for i in input().split():
    if len(i) >= 6:
        if i[-6:] == "Cheese":
            arr.add(i)

if len(arr)> 3:
    print("yummy")
else:
    print("sad")