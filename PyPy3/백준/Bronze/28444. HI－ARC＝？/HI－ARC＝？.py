import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

arr = list(map(int, input().split()))

print(arr[0]*arr[1] - arr[2]*arr[3]*arr[4])