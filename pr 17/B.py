a = input('введите строку ')
b = input('что меняем ')
c = input('чем заменить ')
d = [i for i in a.split(b)]
print('результат:\n' + c.join(d))
