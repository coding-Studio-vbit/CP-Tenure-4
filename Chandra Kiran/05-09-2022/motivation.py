for _ in range(int(input())):
    n,x = map(int,input().split())
    movies = []
    for _ in range(n):
        movies.append(list(map(int,input().split())) )
    
    movies.sort(key=lambda x:x[1], reverse=True)
    for i in movies:
        if i[0] <= x:
            print(i[1])
            break