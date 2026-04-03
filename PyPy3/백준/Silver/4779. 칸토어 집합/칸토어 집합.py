import sys
import math
input = sys.stdin.readline


def MakeBlank(x, p, q):
    if p ==q :
        return "-"
    
    space = (q-p+1)//3
    left = MakeBlank(x, p, p+space-1)
    return left + " " * space + left


while(True):
    try:
        ans = "-" * (3**int(input())) 

        print(MakeBlank(ans,0 ,len(ans)-1))
    except:
        break