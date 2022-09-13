t = int(input())
while(t):
    d,c = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    s1 = sum(l1)
    s2 = sum(l2)
    t2 = s1 + s2 + 2*d
    t1 = s1 + s2    
    
    if(s1>=150 and s2>=150):
        t1 = t1 + c 
    elif(s1<150 and s2<150):
        t1 = t2
    else:
        t1 = t1 + c + d
    
    if(t1<t2):
        print("YES")
    else:
        print("NO")
    
    t-=1