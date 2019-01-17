__author__ = "Doan Phan Thanh"
'''
@Contest: Olympic CP 2019 Round 3
@Problem: A
http://oj.hueuni.edu.vn/contest/194/problem/660/details
'''

def main():
    '''
    @param
    @return
    '''
    n = str(input())
    if int(n) < 10:
        print(n)
    else:
        sumn = sum(int(x) for x in n)
        if sumn < 9*(len(n) - 1):
            sumn = 9*(len(n) - 1)
        if sumn < (int(n[0]) - 1) + 9*(len(n) - 1):
            sumn = (int(n[0]) - 1) + 9*(len(n) - 1)
        print(sumn)
main()
