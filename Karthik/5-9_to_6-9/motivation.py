# cook your dish here
for i in range(int(input())):
    n,x=map(int,input().split())
    s=[]
    r=[]
    for i in range(n):
        a,b=map(int,input().split())
        s.append(a)
        r.append(b)
    max=0
    for i in range(n):
        if s[i]<=x and r[i]>max:
            max=r[i]
    print(max)