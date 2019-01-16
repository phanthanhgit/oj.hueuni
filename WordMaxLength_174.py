__author__ = "Doan Phan Thanh"
'''
Problem WordMaxLength
http://oj.hueuni.edu.vn/practice/problem/174/details
'''

from sys import stdin, stdout

def main():
    '''
    @param
    @return
    '''
    t = int(input())
    for _ in range(t):
        s = stdin.readline()
        smax = 0
        sub = 0
        for i in s:
            if not i == "," and not i == " " and not i == ";" and not i == ":" and not i == ".":
                sub += 1
            else:
                if sub > smax:
                    smax = sub
                sub = 0
        if sub > smax:
            smax = sub
        print("%d\n" % smax)
    
main()
