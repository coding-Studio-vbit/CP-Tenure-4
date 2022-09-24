for g in range(int(input())):
    s = str(input())
    ans = True
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    
    if s[:2] == "</" and s[-1] == ">" and len(s)>3:
        for i in s[2:-1]:
            if i not in a:
                ans = False
                break
    else:
        ans = False
    
    if ans:
        print("Success")
    else:
        print("Error")
