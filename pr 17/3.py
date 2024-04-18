s = input('введите строку:\n')
f = False
count = 0
m=0
c=0
for i in range(len(s)):
    if s[i] != " " and not f:
        count+=1
        f = True
        c += 1
    elif s[i] != " " and f:
        c +=1
    elif s[i] == " " and f:
        f = False
        if c > m:
            m = c
if c > m:
    m = c

#print(f'Найдено слов {count}')
print(f'Самое длинное слово: {m}')