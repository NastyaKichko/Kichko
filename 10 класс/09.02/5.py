def f(a,b):
    if b==0:
        return a
    else:
        return f(b,a%b)

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
f1=f(a,b)
print(f'НОД({a},{b}) = {f1}')
