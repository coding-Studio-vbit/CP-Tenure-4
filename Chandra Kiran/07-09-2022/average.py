for _ in range(int(input())):
    n,k,v = map(int, input().split())
    array = list(map(int, input().split()))
    
    x = int((v*(n+k) - sum(array)) / k)
    
    if int((sum(array) + k*x)/(n+k)) == v and x >0:
        print(x)
    else:
        print(-1)