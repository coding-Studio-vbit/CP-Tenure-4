# cook your dish here

def coupon(test):
    while(test):
        deliv,poc = map(int,input().split())
        d1 = list(map(int,input().split()))
        d2 = list(map(int,input().split()))
        totalcost = sum(d1) + sum(d2) + 2*deliv
        cost_wd = sum(d1) + sum(d2)
        
        if sum(d1)>=150 and sum(d2)>=150:
            cost_wd += poc
        elif sum(d1)>=150 or sum(d2)>=150:
            cost_wd += poc + deliv
        else:
            cost_wd = totalcost
        
        if totalcost > cost_wd:
            print("YES")
        else:
            print("NO")
        
        test-=1

test = int(input())
coupon(test)