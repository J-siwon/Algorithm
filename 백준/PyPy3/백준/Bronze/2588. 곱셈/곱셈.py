import sys
input = sys.stdin.readline

def main():
    a = int(input())
    b = int(input())
    x = b // 100
    y = b % 100
    z = y % 10

    aa= a * z
    aaa = a * (y//10)
    aaaa = a * x

    print(aa)
    print(aaa)
    print(aaaa)
    print(aa + aaa * 10 + aaaa * 100)

if __name__ == "__main__":
    main()