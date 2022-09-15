t = int(input())
while(t):
    n,m = map(int, input().strip().split())
    shoes = 2*n 
    l = 0
    if(n<m):
        l = n 
    else:
        l = m
    
    print(shoes - l)
    t-=1