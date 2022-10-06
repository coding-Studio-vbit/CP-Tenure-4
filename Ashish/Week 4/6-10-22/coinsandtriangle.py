t = int(input())
for i in range(t):
    n = int(input())
    j = 1
    k = 0
    while(n >= j):
        k += 1
        n -= j
        j += 1
    print(k)