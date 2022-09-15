# cook your dish here
for i in range(int(input())):
    n,k,v=map(int,input().split())
    a=list(map(int,input().split()))
    remainingsum=(v*(n+k))-sum(a)
    if remainingsum%k==0 and remainingsum>1:
        print(remainingsum//k)
    else:
        print(-1)