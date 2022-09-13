n = int(input())
for i in range(n):
    flag = "NO"
    d, c = list(map(int, input().split()))
    day1 = list(map(int, input().split()))
    day2 = list(map(int, input().split()))
    Ssum = sum(day1)+2*d+sum(day2)
    if(sum(day1) >= 150 and sum(day2) >= 150):
        if(c < d*2):
            flag = "YES"
    elif(sum(day1) >= 150 or sum(day2) >= 150):
        if(sum(day1)+d+sum(day2)+c < Ssum):
            flag = "YES"
    print(flag)
