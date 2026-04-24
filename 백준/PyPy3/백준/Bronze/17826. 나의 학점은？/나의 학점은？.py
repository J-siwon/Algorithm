import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

arr = list(map(int, input().split()))
x = int(input())
arr.append(x)
arr = sorted(arr, reverse= True);
for i in range(len(arr)):
    if arr[i] == x:
        if i+1 >5:
            if i+1 > 15:
                if i+1 > 30:
                    if i+1 > 35:
                        if i+1 > 45:
                            if i+1 > 48:
                                print("F")
                            else:
                                print("C0")
                        else:
                            print("C+")
                    else:
                        print("B0")
                else:
                    print("B+")
            else:
                print("A0")
        else:
            print("A+")
        break