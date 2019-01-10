from sys import stdin, stdout

def _pow(a, b):
    return a**b

#main
t = int(input())
for _ in range(t):
    a , b = map(float, stdin.readline().rstrip().split())
    print("%.6f" % round(_pow(a, b), 6))
          
