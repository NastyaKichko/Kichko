from random import randint

A = [randint(140,200) for _ in range(35)]
print(f'Рост:\n{" ".join(str(i) for i in A)}')
#k=sum(1 for i in A if i>170)
#if k>=5:
#    print('Количество учеников с ростом больше 170: ',k)
max_h=max(A)
k=A.count(max_h)

#print('Максимальное значение: ', max)
print('Количество максимальных элементов: ', k)