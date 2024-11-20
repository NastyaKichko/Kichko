s = input('введите строку:\n')
m=0
l=""
c=""
w=False
for i in range(len(s)):
    if s[i] != " ":
        c+=s[i]
        w = True
    elif w:
        if len(c) > m:
            m = len(c)
            l = c
        c=""
        w = False

if len(c) > m:
    l = c
    m = len(c)

print(f'Самое длинное слово: {l}, длина {m}')