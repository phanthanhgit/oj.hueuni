__author__ = 'Doan Phan Thanh'
'''
Olympic CP 2019 Round 2
Link problem:
http://oj.hueuni.edu.vn/contest/192/problem/652/details
'''

def main():
    s = raw_input()
    x = 0
    y = 0
    go = [0, 0, 0, 0]
    ok = False
    for c in s:
        if c == 'S':
            go[0] = 1
        elif c == 'N':
            go[1] = 1
        elif c == 'W':
            go[2] = 1
        elif c == 'E':
            go[3] = 1
    if go[0] and go[1] and not go[2] and not go[3]:
        ok = True
    if not go[0] and not go[1] and go[2] and go[3]:
        ok = True
    if go[0] and go[1] and go[2] and go[3]:
        ok = False
    if ok:
        print("Yes")
    else:
        print("No")
main()
