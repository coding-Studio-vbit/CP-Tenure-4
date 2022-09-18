# cook your dish here
for i in range(int(input())):
    n=int(input())
    s=input()
    b=[0 for i in range(n)]
    right=n-1
    left=0
    vowelc=0
    vowels=['a','e','i','o','u']
    for i in reversed(range(n)):
        if vowelc%2==0:
            b[right]=s[i]
            right-=1
        else:
            b[left]=s[i]
            left+=1
        if s[i] in vowels:
            vowelc+=1
    print(''.join(b))