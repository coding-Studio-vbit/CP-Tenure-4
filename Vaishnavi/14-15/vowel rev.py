vo = 'aeiou'
for _ in range(int(input())):
    n = int(input())
    s = input()
    res = ['0']*n
    l,r = 0,n-1
    flag = False
    for i in range(n-1,-1,-1):
        if flag:
            res[l] = s[i]
            l += 1 
        else:
            res[r] = s[i]
            r -= 1 
        if s[i] in vo:
            flag = not flag
    print(''.join(res))
            