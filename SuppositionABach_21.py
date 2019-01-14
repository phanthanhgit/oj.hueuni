__author__ = "Doan Phan Thanh"
'''
Problem: SuppositionABach
http://oj.hueuni.edu.vn/practice/problem/21/details
'''

import math
from sys import stdin, stdout

def main():
    a = []
    for i in range(2, 1001):
        ok = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                ok = False
                break
        if ok:
            a.append(i)
    t = int(raw_input())
    for _ in range(t):
        n, k = map(int, raw_input().split())
        rk = 0
        j = 0
        while j < len(a) and a[j] <= n:
            i = 0
            while i < len(a) and a[i] <= a[j]/2:
                #print ("1 + %d + %d = %d (%d)" %(a[i], a[i+1], 1 + a[i] + a[i+1], a[j]))
                if 1 + a[i] + a[i+1] == a[j]:
                    rk += 1
                    break
                i += 1
            j += 1
        if rk >= k:
            print("YES")
        else:
            print("NO")

main()
