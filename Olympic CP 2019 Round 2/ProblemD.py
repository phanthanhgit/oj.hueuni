__author__ = "Doan Phan Thanh"
'''
Olympic CP 2019 Round 2
Link problem D:
http://oj.hueuni.edu.vn/contest/192/problem/655/details
'''

def solve(n):
    ans = 0
    i = 1
    res = []
    while ans < n and i <= n:
        if n - ans >= i:
            ans += i
            res.append(i)
        else:
            tmp = n - ans
            ans += tmp
            res.pop()
            res.append((i - 1) + tmp)
        i += 1
    for x in res:
        print(x)    
    
if __name__ == "__main__":
    n = int(raw_input())
    solve(n)
    
