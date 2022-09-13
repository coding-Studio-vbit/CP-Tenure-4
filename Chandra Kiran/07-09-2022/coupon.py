# cook your dish here
for _ in range(int(input())):
    d,c = map(int, input().split())
    a1,a2,a3 = map(int, input().split())
    b1,b2,b3 = map(int, input().split())
    day_1 = a1+a2+a3
    day_2 = b1+b2+b3

    count = 2
    total_cost = day_1+day_2
    
    if day_1 < 150:
        total_cost+=d
        count-=1
        
    if day_2 < 150:
        total_cost+=d
        count-=1
    
    
    if count == 2 or count == 1:
        total_cost = total_cost  + c
    
    if total_cost < day_2+day_1+(2*d):
        print("YES")
    else:
        print("NO")