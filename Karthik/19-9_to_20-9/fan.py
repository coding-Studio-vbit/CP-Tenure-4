def activityNotifications(expenditure, d):
    # Write your code here]
    from bisect import bisect_left, insort
    count = 0
    r = [expenditure[i] for i in range(d)]
    r.sort()
    f = expenditure[0]
    mid = d//2
    even = 0 if d%2 else 1    
    for i in range(len(expenditure)-d):
        m = (r[mid] + r[mid-even])/2
        g = bisect_left(r, f)        
        f = expenditure[i+1]
        r.pop(g)
        insort(r, expenditure[i+d])
        if expenditure[i+d] >= m*2:
            count += 1        
    print(count)
activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)