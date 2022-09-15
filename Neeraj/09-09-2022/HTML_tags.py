for _ in range(int(input())):
    s = input().strip()
    n = len(s)
    aplhanumerics = "0123456789abcdefghijklmnopqrstuvwxyz"
    flag = True
    
    if n<=3:
        flag = False
    elif s[1]!= "/" or s[0] != "<":
        flag = False
    elif s[-1]!= ">":
        flag = False
    else:
        for i in s[2:-1]:
            if i not in aplhanumerics:
                flag = False
                break
            
    if flag:
        print("success")
    else:
        print("error")
