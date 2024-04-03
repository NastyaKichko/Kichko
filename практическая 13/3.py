from random import randint

A = [randint(140,200) for _ in range(30)]
print(f'Рост:\n{" ".join(str(i) for i in A)}')
k=sum(1 for i in A if i>170)
if k>=5:
    print('Количество учеников с ростом больше 170: ',k)
    print('Команду можно сформировать')
else:
    print('Количество учеников с ростом больше 170: ',k)
    print('Команду нельзя сформировать')