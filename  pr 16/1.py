from random import randint

n = int(input('Введите количество элементов:\n'))
A = [randint(1,10) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
k = sorted(A[:len(A)//2])
c = sorted(A[len(A)//2:], reverse=True)
l = k + c
print(f'После сортировки:\n{" ".join(str(i) for i in l)} ')