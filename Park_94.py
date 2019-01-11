__author__ = "Doan Phan Thanh"
'''
Problem "Park":
http://oj.hueuni.edu.vn/practice/problem/94/details
'''
fst = 10102010
data = []

#create data
for i in range(8000):
    data.append(0)
    
def main():
    k = int(raw_input())
    res = 0
    for _ in range(k):
        x = int(raw_input())
        if data[x - fst] == 0:
            res += 100
        data[x - fst] += 1
        if data[x - fst] > 5:
            res += 1
    print(res)
main()
