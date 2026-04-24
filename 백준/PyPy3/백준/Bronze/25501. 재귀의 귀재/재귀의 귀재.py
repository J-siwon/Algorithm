import sys
import math
input = sys.stdin.readline

def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

def countrecur(s, l, r, c):
    if l >= r: 
        c+=1
        return c
    elif s[l] != s[r]: 
        c+=1
        return c
    else: 
        c+=1
        return countrecur(s, l+1, r-1, c)

for i in range(int(input())):
    a = input().strip()
    print(str(isPalindrome(a)) + " " + str(countrecur(a, 0 , len(a)-1, 0)))
