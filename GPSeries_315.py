__author__ = "Doan Phan Thanh"
'''
Problem "G.P (geometric progression) series"
http://oj.hueuni.edu.vn/practice/problem/315/details
'''

def main():
    t = int(input())
    for _ in range(t):
        n0, n, d = map(float, input().split())
        s = 0
        for i in range(int(n)):
            s += n0*(d**i)
            print(n0*(d**i))
        print("%.4f" % s)
main()
