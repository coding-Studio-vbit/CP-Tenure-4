t=int(input())
for i in range(t):
    try:
        n,x=map(int,input().split()) #imput for number of movies and hard disk space
        imdb=[]
        for i in range(int(n)):
            l=list(map(int,input().split()))[:2]
            if l[0]<=int(x):
                imdb.append(l[1])
        print(max(imdb))
    except:
        pass
        break