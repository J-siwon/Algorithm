import sys
import math
from collections import deque
input = sys.stdin.readline

def W(a,b,c):
    if a<= 0 or b<= 0 or c<= 0:
        return 1
    
    if a > 20 or b > 20 or c>20:
        return arr[20][20][20]
    
    if a<b and b<c:
        return arr[a][b][c-1] + arr[a][b-1][c-1] - arr[a][b-1][c]
    
    return arr[a-1][b][c] + arr[a-1][b-1][c] + arr[a-1][b][c-1] - arr[a-1][b-1][c-1]

a,b,c = map(int, input().split())
x = 50
arr = [[[0 for _ in range(x+1)]for _ in range(x+1)]for _ in range(x+1)]

for i in range(x+1):
    for j in range(x+1):
        for k in range(x+1):
            arr[i][j][k] = W(i,j,k)

while(a != -1 or b != -1 or c != -1):
    print("w({0}, {1}, {2}) =".format(a,b,c), end = " ")
    if a< 0 :
        a = 0
    if b< 0:
        b = 0
    if c<0:
        c= 0
    print(W(a,b,c))
    a,b,c = map(int, input().split())