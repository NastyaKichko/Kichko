from random import randint

n = int(input('Введите количество элементов:\n'))
A = [randint(-100,100) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
B = [i for i in A if i > 0]
C = [i for i in A if i <= 0]
B.sort(reverse=True)
C.sort()
A = B + C
print('Результат:',*A)
print('Количесиво положительных элеиентов: ', len(B))