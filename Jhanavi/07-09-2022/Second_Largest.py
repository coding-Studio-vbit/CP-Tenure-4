n=int(input())
s=[]
for k in range(n):
    l=list(map(int,input().split()))
    l.sort()
    print(l[-2])
