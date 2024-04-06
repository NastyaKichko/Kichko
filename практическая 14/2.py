from random import randint

n = int(input('Введите количество элементов:\n'))
A = [randint(0,5) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
max=min=0
for i in range(1,n):
    if A[i]>A[max]:
        max=i
    elif A[i]<A[min]:
        min=i

print('Максимальный элемент: ', f'A[{max+1}]={A[max]}')
print('Минимальный элемент: ', f'A[{min+1}]={A[min]}')