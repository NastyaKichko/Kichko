a, b, c = [int(i) for i in input(f'введите три числа: ')]
if a == b == c:
    print('все числа одинаковые')
elif a == b or b == c or a == c:
    print('два числа одинаковые')
else:
    print('нет одинаковых чисел')