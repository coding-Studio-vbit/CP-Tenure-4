n = int(input())
for num in range(n):
    lines, space = map(int, input().split())
    list1 = []
    for line in range(lines):
        list1.append(list(map(int, input().split())))
    for items in list1:
        if(items[0] > space):
            list1.remove(items)
    max = 0
    for i in range(len(list1)):
        if(list1[i][1] > max):
            max = list1[i][1]
    print(max)
