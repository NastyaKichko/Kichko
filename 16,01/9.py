a = int(input('начальный пароль: '))
b = a // 100 + (a % 100) // 10
c = (a % 100) // 10 + a % 10
if c < b :
    d = str(b) + str(c)
else:
    d = str(c) + str(b)
print('пароль: ', d)
