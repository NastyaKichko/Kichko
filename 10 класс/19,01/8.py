a = 0
b = 0
c = 1
while c != 0:
    c = int(input('Введите число: '))
    if c > 0:
        a += 1
    elif c < 0:
        b += 1
    else:
        break
print('Кол-во положительных чисел:', a)
print('Кол-во отрицательных чисел:', b)