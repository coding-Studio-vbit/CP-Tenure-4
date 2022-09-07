# cook your dish here
t = int(input())
while(t):
    try:
        n,x = map(int, input().split())
        space = []
        for i in range(0,int(n)):
            lst = list(map(int,input().split()))[:2]
            if lst[0]<=int(x):
                space.append(lst[1])
        print(max(space))
        
    except:
        pass
        break
    
    
            