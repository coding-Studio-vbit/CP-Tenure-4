# cook your dish here
t = int(input())
for i in range(t):
    try:
        n,m = map(int,input().split())
        if m>=n:
            print(n) 
        else:
            print(2*n-m)
    except:
        pass
        break
        