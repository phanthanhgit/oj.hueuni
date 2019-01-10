import sys
import math
from sys import stdin, stdout

a, b, c = map(float, stdin.readline().rstrip().split())
if(a + b > c and a + c > b and b + c > a):
    p = float((a + b + c)/2)
    res = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(round(res, 2))
else :
    print("No Solution")
