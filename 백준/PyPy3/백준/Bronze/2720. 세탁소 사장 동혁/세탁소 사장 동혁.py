import sys
input = sys.stdin.readline

time = int(input())
a = [[0] * 4 for i in range(time)]

for i in range(time):
    x = int(input())
    rem = x
    while(rem>= 5):
        while(rem>=10):
            while(rem>=25):
                a[i][3] = x // 25
                rem = x % 25
            a[i][2] = rem // 10
            rem = rem % 10
        a[i][1] = rem // 5
        rem = rem % 5
    a[i][0] = rem

for i in range(time):
    print(*a[i][::-1])