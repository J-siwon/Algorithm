import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    print('I LOVE CBNU')
else:
    print('*' * n)
    print(' ' * (n//2), end = '')
    print('*')

    for i in range(1,n//2+1):
        x = (n//2 - i)
        print(' ' * x, end = '')
        print('*', end = '')
        print(' ' * (n - 2*x-2), end = '')
        print('*', end = '')
        if i != n//2:
            print('')