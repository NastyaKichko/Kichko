from random import randint

n = int(input('Введите количество элементов:\n'))
A = [int(input(f'Введите {i+1}-й элемент: ')) for i in range(n)]
max = A[0]
max_count = 1
for i in range(1,n):
    if A[i] > max:
        max = A[i]
        max_count = 1
    elif A[i] == max:
        max_count += 1

print('Максимальное значение: ', max)
print('Количество элементов: ', max_count)