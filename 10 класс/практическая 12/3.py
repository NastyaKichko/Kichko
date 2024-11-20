a, b = map(int,input('Введите x и b:\n').split())
print('Массив: ')
c=[]
k = a+b*4
for _ in range(5):
    c.append(k)
    k -= b

print(' '.join(str(i) for i in c))