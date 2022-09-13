# cook your dish here
t = int(input())
while(t):
    lst = list(map(int,input().split()))[:3]
    lst.sort()
    print(lst[1])
    t-=1