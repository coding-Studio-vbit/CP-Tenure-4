for _ in range(int(input())):
    x = list(map(int, input().split()))

    x.sort()

    print(x[-2])

