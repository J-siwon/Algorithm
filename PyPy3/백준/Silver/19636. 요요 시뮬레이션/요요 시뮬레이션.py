import sys
import math
from collections import deque, Counter

W, I0, T = map(int, input().split()) #체중, 일일 에너지 섭취량,기초 대사량  , 역치
D, I, A = map(int, input().split()) # 기간, 에너지 섭취량, 활동대사량

w = W
i0 = I0
for i in range(D):
    t = I - (I0+A)
    W += t

if W <= 0:
    print("Danger Diet")
else:
    print(W, I0)

I0 = i0
W = w
for i in range(D):
    t = I - (I0+A)
    W += t
    if abs(t) > T:
        I0 += t // 2

if W <= 0 or I0 <= 0:
    print("Danger Diet")
else:
    print(W, I0, end = " ")
    if i0 - I0 > 0:
        print("YOYO")
    else:
        print("NO")