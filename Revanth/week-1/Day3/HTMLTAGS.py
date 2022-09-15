# cook your dish here
def HtmlTags(tag):
    l = len(tag)
    c = 0
    if tag[0] == '<' and tag[1] == '/' and tag[l-1] == '>':
        for i in tag[2:l-1]:
            if i in "0123456789abcdefghijklmnopqrstuvwxyz":
                c+=1
            else:
                c = 0
                break
    if c!=0:
        print('Success')
    else:
        print('Error')

for _ in range(int(input())):
    string = input().strip()
    HtmlTags(string)
