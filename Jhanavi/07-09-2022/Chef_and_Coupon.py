n = int(input())
for i in range (n):
    d,c = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    day1 = sum(a)
    day2 = sum(b)
    if(day1 >=150 and day2 >=150) :
        total = day1 + day2 + c 
    elif (day1 >=150 or day2 >=150):
        total = day1 + day2 + c + d
    elif (day1 <150 and day2 <150):
        total= day1 + day2 + 2*d
    
    total_1 = day1 + day2 + d + d
    if(total < total_1):
        print("YES")
    else :
        print("NO")
