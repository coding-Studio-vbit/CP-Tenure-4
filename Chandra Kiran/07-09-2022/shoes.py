for _ in range(int(input())):
    n,m = map(int, input().split())
    
    left = n - m
    
    if left < 0:
        left = 0
    print( left + n) 