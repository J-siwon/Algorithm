import sys
import math
from collections import deque, Counter

s = int(input())
t = (~s+1) & 0xFFFFFFFF

count = 0
for i in bin(t ^ s):
    if i == '1':
        count +=1
print(count)