from random import randint

n = int(input('Введите количество элементов:\n'))
A = [randint(0,6) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
k = list(reversed(A[0:n//2])) + list(reversed(A[n//2:]))
print('Результат:',*k)
