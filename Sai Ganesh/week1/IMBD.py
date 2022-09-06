for t in range(int(input())):
    (n,x)=map(int, input().split())
    ls=[]
    for i in range(n):
        (s,r)=map(int, input().split())
        if s<=x:
            ls.append(r)
    print(max(ls))