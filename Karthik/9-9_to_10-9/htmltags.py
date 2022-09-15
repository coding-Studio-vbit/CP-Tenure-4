# cook your dish here

for i in range(int(input())):
    s=input()
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    further=True
    if s[0]=='<' and s[1]=='/' and s[-1]=='>':
        s=s.replace("<","",1)
        s=s.replace("/","",1)
        s=s.replace(">","",1)
        for i in s:
            if i in uppercase:
                further=False
        if further==True:
            if s.isalnum() or s.isalpha() or s.isdigit():
                print("SUCCESS")
            else:
                print("ERROR")
        else:
            print("ERROR")
    else:
        print("ERROR")