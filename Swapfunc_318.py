__author__ = "Doan Phan Thanh"
'''
Problem: SwapFunction
http://oj.hueuni.edu.vn/practice/problem/318/details
'''

from sys import stdin, stdout

def swap(a, b):
    '''
    @param a, b
    @return print a, b
    '''
    tmp = a
    a = b
    b = tmp
    
    print("%d %d\n" % (a, b))
    
def main():
    '''
    Main Fucntion of Program
    
    @param no
    @return no
    '''
    t = int(input())
    for _ in range(t):
        a, b = map(int, raw_input().split())
        swap(a, b)
main()
