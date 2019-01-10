import math
from sys import stdin, stdout

def main():
    n = int(input())
    s = str(n**2)
    k = len(s)
    a = ""
    b = ""
    for i in range(int(k/2)):
        a += s[i]
    for i in range(int(k/2), k):
        b += s[i]
    if int(a) + int(b) == n:
        print("YES")
    else:
        print("NO")
main()
