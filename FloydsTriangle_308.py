def main():
    n = int(input())
    for i in range(1, n+1):
        s = ""
        for j in range(1, i+1):
            if not j%2 == 0 and not i%2 == 0:
                s += "1"
            elif i%2 == 0 and not j%2 == 0:
                s += "0"
            elif i%2 == 0 and j%2 == 0:
                s += "1"
            elif not i%2 == 0 and j%2 == 0:
                s += "0"
            elif i == j:
                s += "1"
                
        print(s)
main()
