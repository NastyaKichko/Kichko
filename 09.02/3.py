def f(n):
    x=0
    while n:
        a = n % 10
        n = n // 10
        x+=a
    return x
k=int(input('Введите 1 число: '))
l=int(input('Введите 2 число: '))
if f(k)>f(l):
    print(f'Сумма цифр {k} = {f(k)} > {l} = {f(l)}')
elif f(k)<f(l):
    print(f'Сумма цифр {k} = {f(k)} < {l} = {f(l)}')
else:
    print(f'Сумма цифр {k} = {f(k)} = {l} = {f(l)}')