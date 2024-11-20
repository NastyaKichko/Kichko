def f(n,s=2):
    if n == 1:
        return []
    if n % s == 0:
        return [s]+f(n//s,s)
    return f(n,s+1)

n = int(input('Введите натуральное число: '))
a = f(n)
result = '*'.join(map(str,a))
print(f'{n}={result}')