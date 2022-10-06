# cook your dish here
for _ in range(int(input())):
    n = int(input())
    i = 1
    while n>0:
        if n >= i:
            n -= i
            i += 1
        else:
            break
    print(i-1)