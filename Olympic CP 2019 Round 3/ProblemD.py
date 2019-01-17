__author__ = "Doan Phan Thanh"
'''
@Contest: Olympic CP 2019 Round 3
@Problem: D
http://oj.hueuni.edu.vn/contest/194/problem/663/details
'''
import math

def main():
    '''
    @param
    @return
    '''
    n = int(input())
    s = 0
    for i in range(n):
        x, y = map(int, input().split())
        if i % 2 == 0:
            s += min(x, y)
        else:
            s -= max(x, y)
    print(s)
    '''
    don't complete
    '''
            

main()
