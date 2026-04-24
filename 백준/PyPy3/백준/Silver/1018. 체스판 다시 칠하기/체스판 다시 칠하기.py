import sys
input = sys.stdin.readline

r, c = map(int, input().split())
a = []
for i in range(r):
    a.append(input().strip())

b= [[0]* c for i in range(r)]
board = [[0] * 8 for i in range(8)]
mincount = 64
for i in range(r-7):
    for j in range(c-7):
        for x in range(8):
            for y in range(8):
                board[x][y] = a[i+x][j+y]
        
        main = "W" 
        main2 = "B"
    
        count = 0
        for x in range(8):
            if x%2 == 0 :
                check = main
            else: 
                check = main2
            for y in range(8):
                if y%2 ==0 :
                    if board[x][y] != check:
                        count += 1
                else:
                    if board[x][y] ==check:
                        count += 1
        main = "B" 
        main2 = "W"
        count2 = 0

        for x in range(8):
            if x%2 == 0 :
                check = main
            else: 
                check = main2
            for y in range(8):
                if y%2 ==0 :
                    if board[x][y] != check:
                        count2 += 1
                else:
                    if board[x][y] ==check:
                        count2 += 1

        if(mincount > min(count, count2)):
            mincount = min(count, count2)
print(mincount)
        

