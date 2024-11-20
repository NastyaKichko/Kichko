def f(n,k=1):
    if n==0:
        return 1
    c=0
    for i in range(k,n+1):
        c+=f(n-i,i)
    return c


n = int(input('Введите натуральное число: '))
result = f(n)-1
print('Кол-во разложений: ', result)