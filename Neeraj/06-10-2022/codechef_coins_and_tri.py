for _ in range(int(input())):
    n = int(input())
    i = 1
    height = 0 
    while i<=n:
        n-=i
        height+=1
        i+=1
    print(height)
