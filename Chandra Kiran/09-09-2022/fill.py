for i in range(int(input())):
    try:
        n,k = map(int,input().split())
        s = input()
        zeros = '0'*k
        count = 0
        if k==1:
            print(s.count('0'))
        else:
            print(s.count(zeros))
            
    except:
        pass
        break