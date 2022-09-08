# cook your dish here
for i in range(int(input())):
    d,c=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    day1=sum(a)
    day2=sum(b)
    if day1>=150 and day2>=150:
        sum1=day1+day2+c
        sum2=day1+day2+d+d
    elif day1>=150 or day2>=150:
        sum1=day1+day2+c+d
        sum2=day1+day2+d+d
    else:
        sum1=day1+day2+d+d
        sum2=0
    if sum1<sum2:
        print("YES")
    else:
        print("NO")