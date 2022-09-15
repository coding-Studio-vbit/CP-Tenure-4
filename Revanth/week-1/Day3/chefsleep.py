# cook your dish here

for _ in range(int(input())):
    n,k = map(int,input().split())
    p = input()
    c,sleep = 0,0
    for j in range(0, len(p)):
        if p[j] == '0':
            c+=1
            if c == k:
                sleep+=1
                c = 0
        else:
            c = 0
    print(sleep)