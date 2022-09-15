for _ in range(int(input())):
    d, c = map(int, input().split())
    day1 = list(map(int, input().split()))
    day2 = list(map(int, input().split()))
    
    cost_With_Coupon = c
    cost_Without_Coupon = 2*d
    
    if sum(day1)<150:
        cost_With_Coupon+=d
    if sum(day2) < 150:
        cost_With_Coupon+=d
    
    if cost_With_Coupon < cost_Without_Coupon:
        print("YES")
    else:
        print("NO")
