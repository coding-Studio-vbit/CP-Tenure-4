test = int(input())
while(test):
    n, m = map(int, input().split())
    if n<=m:
        print(n)
    else:
        print(2*n-m)
    test-=1