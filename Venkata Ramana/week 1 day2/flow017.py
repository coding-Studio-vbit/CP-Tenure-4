t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (b<a<c or c<a<b):
        print(a)
    elif (c<b<a or a<b<c):
        print(b)
    else:
        print(c)