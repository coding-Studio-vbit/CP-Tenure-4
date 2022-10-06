# cook your dish here
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    i=0
    j=len(arr)-1
    x=arr[i]
    y=arr[j]
    while((j-i)>1):
        if(x<y):
            i+=1
            x+=arr[i]
        else:
            j-=1
            y+=arr[j]
    print(max(x,y))