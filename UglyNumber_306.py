import sys
from sys import stdin, stdout

#main
n = int(input())
while n > 1:
    if n % 2 == 0:
        n = int(n/2)
    elif n % 3 == 0:
        n = int(n/3)
    elif n % 5 == 0:
        n = int(n/5)
    else:
        print("NO")
        sys.exit()
print("YES")
        
