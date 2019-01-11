__author__ = "Doan Phan Thanh"
'''
Problem "Rangeof2Num":
http://oj.hueuni.edu.vn/practice/problem/15/details
'''

def main():
    #x, y = map(int, raw_input().split())
    x, y = map(int, input().split())
    if x == y or y == x + 1:
        print(0)
    else:
        x += 1
        y -= 1
        print(y - x + 1)
        for i in range(x, y + 1):
            if i != 0:
                #print i,
                print(i, end="") 
main()
