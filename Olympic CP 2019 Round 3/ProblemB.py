__author__ = "Doan Phan Thanh"
'''
@Contest: Olympic CP 2019 Round 3
@Problem: B
http://oj.hueuni.edu.vn/contest/194/problem/661/details
'''

def main():
    '''
    @param
    @return
    '''
    a = []
    b = []
    n = int(input())
    for _ in range(n):
        ai, bi = map(int, raw_input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n - 1, -1, -1):
        if (a[i] + ans) % b[i] == 0:
            continue
        else:
            ans += int(b[i] - ((a[i] + ans) % b[i]))
    print(ans)
    
main()
