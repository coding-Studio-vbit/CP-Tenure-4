for i in range(int(input())):
    n,m=map(int,input().split())
    print(n) if m>=n else print(2*n-m)