n = int(input())
an = "1234567890qwertyuiopasdfghjklzxcvbnm"
for i in range(n):
    string = input().strip()
    temp = string[2:len(string) - 1]
    flag = False
    if string[0:2] == '</' and string[-1] == '>' and len(temp):
        for c in temp:
            if c not in an:
                print('Error')
                flag = True
                break
        if not flag:
            print('Success')
    else:
        print('Error')
