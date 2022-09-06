# cook your dish here
t = int(input())
while(t):
    l1 = list(map(int, input().split()))
    n,x = l1[0],l1[1]
    m = 0
    for i in range(0, n):
        l2 = list(map(int, input().split()))
        s,r = l2[0], l2[1]
        if(s<=x and r>=m):
            m = r
    print(m)
    t-=1