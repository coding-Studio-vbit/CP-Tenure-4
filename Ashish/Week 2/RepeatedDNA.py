s = 'AAAAAAAAAAAAA'
i = 0
j = 10
a = set()
while j <= len(s):
    s1 = s[i:j]
    if s.count(s1) > 1:
        a.add(s1)
        i += 1
        j += 1
print(a)
print(123)