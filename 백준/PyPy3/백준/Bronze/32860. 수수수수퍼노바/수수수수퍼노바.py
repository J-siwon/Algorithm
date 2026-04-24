import sys
import math
from collections import deque, Counter

a,b = map(int, input().split())
left = b%26
alpha = " abcdefghijklmnopqrstuvwxyz"
if b> 26:
    if b%26==0:
        print("SN " + str(a) + alpha[b//26-1] + "z")
    else:
        print("SN " + str(a) + alpha[b//26] + alpha[b%26])
else:
    print("SN " + str(a) + alpha[b].upper())