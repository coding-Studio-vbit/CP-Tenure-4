# cook your dish here
num_tests = int(input())
for t in range(num_tests) :
    D, C = map(int, input().split())
    first_day_order = sum(list(map(int, input().split())))
    second_day_order = sum(list(map(int, input().split()))) 
    
    cost_without_coupon = 2 * D 
    cost_with_coupon = C 
    if first_day_order < 150 : 
        cost_with_coupon += D 
    if second_day_order < 150 : 
        cost_with_coupon += D 
        
    if cost_with_coupon < cost_without_coupon : 
        print("YES")
    else :
        print("NO")