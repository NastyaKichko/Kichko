from random import randint
def b(a,x):
    l = 0
    r = len(a) - 1
    c = 0
    while l <= r:
        mid = (l+r)//2
        c+=1
        if a[mid] == x:
            return True, c
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False, c

A = [randint(1, 10) for _ in range(10)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
A.sort()
print(f'После сортировки:\n{" ".join(str(i) for i in A)}')
x = int(input('Введите x: '))
f, c = b(A,x)
if f:
    print(f'Число {x} найдено')
else:
    print(f'Число {x} не найдено')

print('Количество сравнений:',c)
