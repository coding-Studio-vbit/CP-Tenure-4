for _ in range(int(input())):
    d,c = map(int,input().split())
    day_1 = list(map(int,input().split()))
    day_2 = list(map(int,input().split()))
    wo_coup = sum(day_1)+sum(day_2)+2*d
    w_coup = sum(day_1)+sum(day_2)
    if sum(day_1) >= 150 and sum(day_2) >= 150:
        w_coup += c
    elif  sum(day_1) >= 150 or sum(day_2) >= 150:
        w_coup += (c+d)
    else:
        w_coup = wo_coup
    if w_coup < wo_coup:
        print("YES")
    else:
        print("NO")