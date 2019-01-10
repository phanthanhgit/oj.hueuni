import math
from sys import stdin, stdout

def main():
    t = int(raw_input())
    for _ in range(t):
        st = stdin.readline()
        lst = []
        ans = 0
        for i in range(len(st) - 3):
            if not st[i] == "0":
                s = 0
                s = int(st[i])*100 + int(st[i+1])*10 + int(st[i+2])
                if not s in lst:
                    lst.append(s)
                    ans += 1
        print(ans)
main()
