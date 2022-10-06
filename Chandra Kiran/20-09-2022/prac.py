from math import inf


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    diff = 10**20
    index = 0
    a.sort()
    # print(a)
    for i in range(0,n-2):
        val = (a[i+1] - a[i]) + (a[i+2] - a[i+1])
        if val < diff:
            diff = val
            index = i
    print(diff)