__author__ = "Doan Phan Thanh"
'''
Problem "A.P (arithmetic progression) series"
http://oj.hueuni.edu.vn/practice/problem/314/details
'''

def main():
    t = int(input())
    for _ in range(t):
        n0, n, d = map(int, raw_input().split())
        s = 0
        for i in range(1, n + 1):
            s += n0 + (i - 1)*d
        print(s)
main()
