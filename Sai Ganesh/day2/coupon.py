for i in range(int(input())):
    d,c=map(int,input().split())
    a=input().split()
    b=input().split()
    s1=s2=0
    for i in range(3):
        s1=s1+int(a[i])
        s2=s2+int(b[i])
    t=s1+s2+2*d
    if s1>=150 and s2>=150:
        if s1+s2+c<t:
            print("YES")
        else :
            print("NO")
    elif s1>=150 or s2>=150:
        if s1+s2+c+d<t:
            print("YES")
        else :
            print("NO")
    else :
        if s1+s2+c+2*d<t:
            print("YES")
        else:
            print("NO")