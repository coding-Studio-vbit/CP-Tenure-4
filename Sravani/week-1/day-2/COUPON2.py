t = int(input())
for i in range(t):
    try:
        d,c = map(int,input().split())
        day_1 = list(map(int,input().split()))[:3]
        day_2 = list(map(int,input().split()))[:3]
        coupon = sum(day_2)+ sum(day_1)+ c
        if (sum(day_1)>=150 and sum(day_2)>=150):
            delivery = sum(day_2)+ sum(day_1)+ 2*d
        elif (sum(day_1)>=150 or sum(day_2)>=150):
            delivery = sum(day_2)+ sum(day_1)+ d
        else:
            delivery = sum(day_1) + sum(day_2)
        if coupon<delivery:
            print("YES")
        else:
            print("NO")
    except:
        pass
        break
        
        
    