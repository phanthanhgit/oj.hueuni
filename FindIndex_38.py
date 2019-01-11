__author__ = 'Doan Phan Thanh'
'''
Tim vi tri cua so n
Link problem:
http://oj.hueuni.edu.vn/practice/problem/38/details
'''

def solve(n):
    s = ""
    for i in range(0, n + 1):
        s += str(i)
    res = s.find(str(n))
    print(res)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)
