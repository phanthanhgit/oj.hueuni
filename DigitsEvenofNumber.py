t = int(input())

for _ in range(t):
    n = int(input())
    n = abs(n)
    res = 0
    while n > 0 :
        x = n % 10
        if x % 2 == 0 :
            res += x
        n = int(n / 10)
    print(res)
