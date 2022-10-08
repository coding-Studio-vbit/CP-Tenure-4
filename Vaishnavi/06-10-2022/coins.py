for _ in range(int(input())):
    n = int(input())
    i = 1
    h = 0
    while n >= i:
        n -= i
        i += 1
        h += 1 
    print(h)