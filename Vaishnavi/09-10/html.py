for _ in range(int(input())):
    s = input()
    s = s.replace(' ','')
    n = len(s)
    if s[0] == "<" and s[1] == "/" and s[-1] == '>':
        flag = 0
        s = s[2:n-1]
        string = s
        up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in s:
            if i in up:
                flag = 1 
                break
        if flag == 0:
            if s.isalnum() or s.isalpha() or s.isdigit():
                print("Success")
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("Error")