import sys
import math
from sys import stdin, stdout

#check func
def checkPangram(s):
    #create list of 26 chacecters
    a = []
    for i in range(26):
        a.append(0)
    #processing
    for x in s.upper() :
        if ord(x) >= 65 and ord(x) <= 90 :
            a[ord(x) - ord('A')] = 1
    for c in a :
        if c == 0 :
            return 0
    return 1

#main
n = int(input())
s = ""
for i in range(n):
    s = stdin.readline()
    
    if checkPangram(s) == 1 :
        print("Yes\n")
    else :
        print("No\n")
    
