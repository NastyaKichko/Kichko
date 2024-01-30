n = int(input('введите число N: '))
m = 0
a, b = (0, 1)
while b<n:
    a, b = b, a + b
    m += a
print('сумма: ', m)