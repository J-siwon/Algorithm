import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

x = int(input())
arr = list(map(int, input().split()))
c = Counter(arr)
print(c[int(input())])