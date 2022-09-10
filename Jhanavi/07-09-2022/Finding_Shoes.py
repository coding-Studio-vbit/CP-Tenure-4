t = int(input())
for i in range (t):
    n,m = map(int,input().split())
    if (m > n ):
        print(n)
    elif (m == 0):
        print(n*2)
    else :
        print(n*2-m)
        
