t = int(input())
for _ in range(t):
    h= 0
    n = int(input())
    while n>h and n>0:
        h=h+1
        n=n-h
    print(h)    
