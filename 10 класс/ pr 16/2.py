from random import randint

n = int(input('Введите количество элементов:\n'))
A = [randint(1,10) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
A.sort()
print(f'После сортировки:\n{" ".join(str(i) for i in A)}')
c = len(set(A))
print('Различных чисел: ',c)