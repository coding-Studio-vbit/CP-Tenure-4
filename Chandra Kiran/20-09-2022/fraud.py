import statistics

expenditure = [ 2 ,3 ,4 ,2 ,3 ,6 ,8 ,4, 5]
d = 5
count = 0
rip = []
flag = True
for i in range(0,len(expenditure)):
    median = 0
    
    if(i+d<len(expenditure)):

        if len(rip) == 0:
            rip = expenditure[i:i+d]
            rip.sort()
        else:
            print("before",rip)
            rip.remove(expenditure[i-1])
            x = len(rip) - 1
            while(x>=0 and expenditure[i+d-1] < rip[x]):
                x-=1
                print("rip",x)
            rip.insert(x+1,expenditure[i+d-1])
            print("after",rip)
        
        median = statistics.median(rip)

        if(2*median >= expenditure[i+d]):
            count+=1
print(count)


    

# 2 3 4 2 3 6 8 4 5
# 2 2 3 3 4 | 6

# def activityNotifications(expenditure, d):
#     # Write your code here
#     count = 0
#     rip = []
#     for i in range(0,len(expenditure)):
#         median = 0
        
#         if(i+d<len(expenditure)):
            
#             if len(rip) == 0:
#                 rip = expenditure[i:i+d]
#             else:
#                 rip.remove(expenditure[i-1])
#                 rip.append(expenditure[i+d-1])
#             if len(rip) % 2 == 1:
#                 temp = rip
#                 temp.sort()
#                 median = temp[int(d/2)]
#             else:
#                 temp = rip
#                 temp.sort()
#                 median = int((temp[int(d/2)] + temp[int(d/2)+1] ) / 2)
#             rip = temp
            
#         if(i+d < len(expenditure)):
#             # print("rip",i+d,median,expenditure[i+d])
#             if (expenditure[i+d] >= 2*median):
#                 count+=1
#     return count