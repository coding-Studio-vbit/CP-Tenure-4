t = int(input())
while(t):
    t-=1 
    l = list(map(int, input().split()))
    m = max(l)
    l.remove(m)
    print(max(l))