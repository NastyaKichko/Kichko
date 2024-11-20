a = int(input('введите номер месяца: '))
if a == 12 or a < 3:
    print('зима')
elif a < 6:
    print('весна')
elif a < 9:
    print('лето')
elif a < 12:
    print('осень')
else:
    print('неверный номер месяца')