if __name__ == '__main__':
    t = int(input())
    while(t):
        n = int(input())
        c = 0
        i = 1
        while(n):
            if(n>=i):
                n-=i
                c+=1 
            else:
                break
            i+=1
        
        print(c)
        t-=1
    