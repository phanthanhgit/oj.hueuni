import sys
import math
from sys import stdin, stdout

#main
x1, y1, x2, y2 = map(float, stdin.readline().rstrip().split())
res = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("%.4f" % res)
print(round(res, 4))
