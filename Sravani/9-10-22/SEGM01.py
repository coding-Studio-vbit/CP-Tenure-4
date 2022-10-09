# cook your dish here
for i in range(int(input())):
    num = input()
    
    x= num.count('1')
  
    flag = False
    for i in range(0,len(num)):
        if x!=0 and num[i:i+x]=='1'*x:
            flag = True
    if(flag):
        print("YES")
    else:
        print("NO")
    