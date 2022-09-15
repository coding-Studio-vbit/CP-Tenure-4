t = int(input(""))
for i in range(t):
    s = input().strip()
    uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s1 = s[2:len(s) - 1]
    status = True
    if s[0] == "<" and s[-1] == ">" and s[1]== "/":
        for i in s1:
            if i in uc:
                status = False
        if status == True:
            if s1.isalnum() or s1.isdigit() or s1.isalpha():
                print("Success")
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("Error")