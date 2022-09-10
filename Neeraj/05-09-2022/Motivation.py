for _ in range(int(input())):
    n, x = map(int, input().split())
    a = []
    ans = 0
    for i in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x: x[1],reverse = True)
    for i in range(n):
        if x:
            if a[i][0]<=x:
                print(a[i][1])
                break
    
