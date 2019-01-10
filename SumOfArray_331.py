import sys
import math
from sys import stdin, stdout

def Sum(a, n):
    res = 0
    for x in range(n):
        res += a[x]
    return res

n = int(input())
a = []
for i in map(int, stdin.readline().rstrip().split()):
    a.append(i)
print(Sum(a, n))
