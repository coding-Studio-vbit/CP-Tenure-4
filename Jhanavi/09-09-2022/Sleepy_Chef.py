t = int(input())
for _ in range (t):
    n,k = map(int,input().split())
    s = input()
    x = s.count(k*"0")
    print(x)
