__author__ = "Doan Phan Thanh"
'''
Problem Exp func
http://oj.hueuni.edu.vn/practice/problem/323/details
'''
import math

def myExp(x):
    '''
    @param float: x
    @return float: e^x
    '''
    s = 1 + x
    gt = 1
    for i in range(2, 100):
        gt = gt*i
        s += x**i/gt
    
    return s

def main():
    '''
    @param no
    @return no
    '''
    t = int(raw_input())
    for _ in range(t):
        x = float(raw_input())
        print("%.6f\n" % (myExp(x)))
main()
