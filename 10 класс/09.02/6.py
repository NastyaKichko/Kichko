def f(n):
    a = 0
    while(n>0):
        a=a*10+n%10
        n=n//10
    return a
n=int(input('Введите число: '))
print(f'После переворота: {f(n)}')