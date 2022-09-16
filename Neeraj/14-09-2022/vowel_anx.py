for _ in range(int(input())):
    n = int(input())
    s = input()
    vowels = ["a", "e", "i", "o", "u"]
    
    a = ["0"]*n
    
    l = 0
    r = n-1
    
    deal = False
    for i in range(n-1,-1,-1):
        if deal:
            a[l] = s[i]
            l+=1
        else:
            a[r] = s[i]
            r-=1
        if s[i] in vowels:
            deal = not deal
            
    print("".join(a))
