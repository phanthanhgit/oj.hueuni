import math
from sys import stdin, stdout

#func check
def check(a, n):
    ok = 1
    for i in range(1, n):
        if a[i] < a[i - 1] :
            ok = 0
            break
    return ok

#main
n = int(input())
a = []
for i in map(int, stdin.readline().rstrip().split()):
    a.append(i)
    
if check(a, n):
    print("Yes")
else :
    print("No")
