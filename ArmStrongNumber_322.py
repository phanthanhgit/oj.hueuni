__author__ = "Doan Phan Thanh"
'''
Problem "So Armstrong":
http://oj.hueuni.edu.vn/practice/problem/322/details
'''
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    n = int(raw_input())
    for i in range(153, 100000):
        res = 0
        x = i
        j = 0
        a = []
        while x > 0:
            a.append(x % 10)
            x = int(x / 10)
            j+=1
        for c in a:
            res += c**j
        if res == i:
            data.append(i)
        if len(data) > 22:
            break
    for x in range(0, n):
        print data[x], #python 3 : print(data[x], end=" ")
main()
