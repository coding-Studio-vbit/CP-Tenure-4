for _ in range(int(input())):
    n,x = map(int,input().split())
    rate = 0
    for i in range(n):
        s,r = map(int,input().split())
        if s <= x and r > rate:
            rate = r
    print(rate)