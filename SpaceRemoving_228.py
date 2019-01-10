import sys
import math
from sys import stdin, stdout

#main
n = int(input())
for i in range(n) :
    s = ""
    s = stdin.readline()
    res = ""
    for x in s.strip() :
        if not x == " " :
            res += x
        elif x == " " and not res[len(res) - 1] == " " :
            res += x
    print(res)
