import sys
import math
input = sys.stdin.readline

x = input().strip()
y = input().strip()

nums = "1234567890"
a = ""
for i in x:
    if i in nums:
        continue
    a += i

if y in a:
    print(1)
else:
    print(0)