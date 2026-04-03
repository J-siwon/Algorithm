import sys
input = sys.stdin.readline

x = int(input())

arr = list(map(int, input().split()))
arr2 = []
arr3 = []

arr = arr[::-1]
isPrinted = False
i =1
while(i <= x):
    if len(arr2) > 0:
        if arr2[-1] == i:
            arr3.append(arr2.pop())
            i+=1
            continue
    if(len(arr) >0):
        if arr[-1] == i:
            arr3.append(arr.pop())
            i +=1
        else:
            arr2.append(arr.pop())
    else:
        print("Sad")
        isPrinted = True
        break
        
if(isPrinted == False):
   print("Nice")