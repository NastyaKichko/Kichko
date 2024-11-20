from random import randint

n = int(input('Введите количество элементов:\n'))
A = [randint(-100,100) for _ in range(n)]
print(f'массив:\n{" ".join(str(i) for i in A)}')
k = sum(1 for i in range(1, len(A)) if A[i] * A[i-1]<0)
print(k)