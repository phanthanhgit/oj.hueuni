import math
from sys import stdin, stdout

def main():
    n = int(input())
    for _ in range(n):
        s = stdin.readline() #using raw_input() for python 2
        s = s.upper()
        fs = ""
        for c in s:
            if ord(c) >= 65 and ord(c) <= 90:
                fs += c
        else:
            ok = True
            for i in range(int(len(fs)/2)):
                if fs[i] != fs[len(fs) - 1 - i]:
                    ok = False
                    break
            if ok:
                print("Yes")
            else:
                print("No")
    
main()
    
