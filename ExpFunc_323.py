__author__ = "Doan Phan Thanh"
'''
Problem Exp func
http://oj.hueuni.edu.vn/practice/problem/323/details
'''
import math
from sys import stdin, stdout

p = 0.0000001

def myExp(x):
    '''
    @param float: x
    @return float: e^x
    '''
    sub = 1.0
    s = 1.0
    i = 0
    while abs(sub) >= p:
        i += 1
        sub = sub*x/i
        s += sub
        
    return s

def main():
    '''
    @param no
    @return no
    '''
    t = int(input())
    for _ in range(t):
        x = float(input())
        print("%.6f\n" % myExp(x))
main()
