# cook your dish here
for i in range(int(input())):
    N1,K1=map(int,input().split())
    string1=input()
    COUnt1=0
    ans1=0
    for i in range(N1):
        if string1[i]=='0':
            COUnt1+=1
        else:
            if COUnt1>=K1:
                ans1+=COUnt1//K1

            COUnt1=0    
    ans1+=COUnt1//K1        


    print(ans1)