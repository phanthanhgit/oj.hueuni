__author__ = "Doan Phan Thanh"
'''
Problem 47:
http://oj.hueuni.edu.vn/practice/problem/47/details
'''

def solve(s, i):
    s = s.replace("%", "%25")
    s = s.replace(" ", "%20")
    s = s.replace("!", "%21")
    s = s.replace("$", "%24")
    s = s.replace("(", "%28")
    s = s.replace(")", "%29")
    s = s.replace("*", "%2a")

    print("Case #%d: %s" % (i, s))

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(t):
        s = raw_input()
        solve(s, i+1)
