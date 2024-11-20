n = int(input("Введите значение n: "))
p = int(input("Введите значение p: "))
sum = 0
for i in range(1, n+1):
    bi = int(input("Введите значение b{}: ".format(i)))
    sum += bi
    if sum < p:
        print("Сумма чисел меньше p")
    else:
        print("Сумма чисел больше или равна p")