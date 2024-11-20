a = int(input('введите возраст: '))
if (2 <= a%10 <= 4) and not (11<= a%100 <=14):
    print('вам', a, 'года')
elif a % 10 == 1 and a % 100 != 11:
    print('вам', a, 'год')
else:
    print('вам', a, 'лет')
