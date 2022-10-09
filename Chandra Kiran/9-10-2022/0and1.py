# cook your dish here
for _ in range(int(input())):
    s = input()
    if(not "1" in s):
        print("NO")
        continue

    x = ""
    flag = 1
    for i in s:
        if i == "1" and x == "":
            x = "1"
        if i == "0" and x == "1":
            x = "10"
        if i == "1" and x == "10":
            print("NO")
            flag = 0
            break
    
    if flag:
        print("YES")