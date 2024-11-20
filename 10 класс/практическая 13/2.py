from random import randint

n = int(input('Введите количество элементов:\n'))
A = [randint(1,100) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
r=0
for i in range(n):
    if i%2==0:
        r+=A[i]
    else:
        r-=A[i]

print('Знакопеременная сумма: ',r)