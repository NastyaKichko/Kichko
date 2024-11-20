from random import randint

n = int(input('Введите количество элементов:\n'))
A = [randint(1,20) for _ in range(n)]
print(f'массив:\n{" ".join(str(i) for i in A)}')
k = 0
s = 0
for i in A:
    if i % 2!= 0:
        s+=1
        k= max(k,s)
    else:
        s=0
print(k)