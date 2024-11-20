def dig(a):
    for i in range (2,a):
        if a % i == 0:
            return True
    return False
a=int(input('введите натуральное число: '))
if dig(a):
    print(f'число {a} совершенное')
else:
    print(f'число {a} не совершенное')