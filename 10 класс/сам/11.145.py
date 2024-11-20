from random import randint

n = int(input('Введите количество элементов:\n'))
A = [randint(1,100) for _ in range(n)]
print(f'массив:\n{" ".join(str(i) for i in A)}')
for i in range(0, len(A), 2):
    A[i], A[i+1]=A[i+1],A[i]
print('результат: ', *A)