import sys
import math
input = sys.stdin.readline

x = float(input())
while(x != -1):
    print("Objects weighing " +(format(x,".2f")) + " on Earth will weigh " + format(x * 0.167, ".2f") + " on the moon.")
    x = float(input())