for _ in range(int(input())):
    n = int(input())
    string = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    ans = ['0'] * n
    op= False
    right = 0
    left = n-1
    for i in reversed(range(n)):
        if(op):
            ans[right] = string[i]
            right += 1
        else:
            ans[left] = string[i]
            left -= 1
        if(string[i] in vowels):
            op = not op
    print(''.join(ans))
        
# // abcdefghij 
# dcbaefghij
# hgfeabcdij
# // hgfeabcdij
