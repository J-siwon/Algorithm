import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    if n ==0:
        print(0)
        continue
    if n < 0:
        n = -n
        a = int(math.log2(n))
        if n == 2**a:
            print(7 * 2**a-4)
        else:
            print(7 * 2**a-4  +  5*2**a + n )
    else:
        a = int(math.log2(n))
        b = n - 2**a
        if b == 0:
            print(7 * 2**a-4 - 2*2**a)
        else:
            print(7 * 2**a-4 + 2**a + n)