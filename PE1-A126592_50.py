t = int(input())
for i in range(t) :
    n = int(input())
    res = 0
    res += int(((n - (n % 3) + 3)*((n - (n % 3) - 3)/3 + 1))/2);
    res += int(((n - (n % 5) + 5)*((n - (n % 5) - 5)/5 + 1))/2);
    res -= int(((n - (n % 15) + 15)*((n - (n % 15) - 15)/15 + 1))/2);
    print(res%(10**9 + 7))
