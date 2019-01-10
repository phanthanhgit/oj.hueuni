__author__ = 'Doan Phan Thanh'
'''
Project Basic Python
Machine Learning
https://github.com/phanthanhgit/oj.hueuni
'''

#from sys import stdin

def solve(t):
    for _ in range(t):
        st = raw_input()
        lst = []
        ans = 0
        for i in range(len(st) - 3):
            if not st[i] == '0':
                s = 0
                s = int(st[i])*100 + int(st[i+1])*10 + int(st[i+2])
                if not s in lst:
                    lst.append(s)
                    ans += 1
        print(ans)

if __name__ == "__main__":
    t = int(raw_input())
    solve(t)
