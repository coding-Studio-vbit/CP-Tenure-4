for _ in range(int(input())):
    n,m = map(int,input().split())
    if m > n:
        print(n)
    else:
        print((2*n)-m)