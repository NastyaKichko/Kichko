from random import randint

A = [randint(50,150) for _ in range(25)]
print(f'Вес:\n{" ".join(str(i) for i in A)}')
s1=sum(i for i in A if i>100)
c1=sum(1 for i in A if i>100)
s2=sum(i for i in A if i<=100)
c2=sum(1 for i in A if i<=100)
k=s1/c1
p=s2/c2
print('Средняя масса полных: ',k)
print('Средняя масса не полных: ',p)
