import math
from sys import stdin, stdout

x, y, z = map(float, stdin.readline().rstrip().split())

c = float(x - x**2/6 + x**5/120)
a = float((3 + math.exp(y - 1))/(1 + x**2 * abs(y - math.tan(z))))
b = float(1 + abs(y - x) + (y - x)**2/2 + (y - x)**3/3)

#print("%.4f" % round(a, 4))
#print("%.4f" % round(b, 4))
#print("%.4f" % round(c, 4))

print("%.4f" % a)
print("%.4f" % b)
print("%.4f" % c)
