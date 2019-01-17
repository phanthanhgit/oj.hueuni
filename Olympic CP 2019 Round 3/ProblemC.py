__author__ = "Doan Phan Thanh"
'''
@Contest: Olympic CP 2019 Round 3
@Problem: C
@Link: http://oj.hueuni.edu.vn/contest/194/problem/662/details
'''

def main():
    '''
    @param
    @return
    '''
    n = int(input())
    a = []
    ans = 0
    if n == 1:
        print(0)
        return
    for _ in range(n):
        x = int(raw_input())
        a.append(x)
        ans = max(ans, x)
        
    for i in range(1, n - 1):
        ans += min(max(a[i], a[i-1]), max(a[i], a[i+1]))
        a[i] = max(max(a[i], a[i-1]), max(a[i], a[i+1]))
        
    print(ans)

main()
