__author__ "Doan Phan Thanh"
'''
Problem
http://oj.hueuni.edu.vn/practice/problem/298/submission
'''

import math
#main
x1, y1, x2, y2 = map(int, raw_input().split())
res = float(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

print("%.4f" % res)
