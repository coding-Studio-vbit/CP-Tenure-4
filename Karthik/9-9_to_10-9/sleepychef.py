# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    nap="0"*k
    totnap=s.count(nap)
    print(totnap)