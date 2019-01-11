__author__ = "Doan Phan Thanh"
'''
Problem "Sinh so theo quy luat":
http://oj.hueuni.edu.vn/practice/problem/197/details
'''

def main():
    t = int(input())
    for _ in range(t):
        p = int(input())
        i = 1
        while i <= 301 and p > 1:
            if p % 2 == 0:
                p = int(p / 2)
            else:
                p = 3*p + 1
            i+=1
        if i > 300:
            print("Infinite (sup)")
        else:
            print(i)
main()
