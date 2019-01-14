__author__ = "Doan Phan Thanh"
'''
Problem "DectoBin"
http://oj.hueuni.edu.vn/practice/problem/310/details
'''

def main():
    n = int(raw_input())
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n = int(n / 2)
    print(s)
main()
