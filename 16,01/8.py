a = int(input('стоимость(в млн): '))
b = int(input('площадь: '))
i = 0
if a <= 10 and b >= 100:
    i += 1
elif a <= 7 and b >= 80:
    i += 1
if i == 1:
    print('подходит')
else:
    print('не подходит')