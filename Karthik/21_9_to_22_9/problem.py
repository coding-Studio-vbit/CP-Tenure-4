

from math import inf


for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    mini=inf
    arr.sort()
    for i in range(1,len(arr)-1):
        mini=min(mini,arr[i]-arr[i-1]+arr[i+1]-arr[i])
    print(mini)
             