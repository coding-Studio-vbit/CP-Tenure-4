for i in range(int(input())):
    n = int(input())
    string = input()
    s = [0 for i in range(n)]
    l, r = 0, n-1
    c = 0
    vowels = ['a','e','i','o','u']
    for i in reversed(range(n)):
        if c % 2 == 0:
            s[r] = string[i]
            r -= 1
        else:
            s[l]=string[i]
            l += 1
        if string[i] in vowels:
            c += 1
    print(''.join(s))