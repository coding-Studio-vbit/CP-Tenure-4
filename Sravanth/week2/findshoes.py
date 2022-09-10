# cook your dish here
num = int(input())
for i in range(num):
    n, m = map(int, input().split())
    if(n < m):
        print(n)
    else:
        print((2*n)-m)
