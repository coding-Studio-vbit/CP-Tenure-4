for i in range(int(input())):
  
    n = int(input())
    c = 0
    i = 1
    while(i<=n):
        n-=i
        i += 1
        c += 1
    print(c)