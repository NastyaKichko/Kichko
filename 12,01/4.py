a, b, c = map(int, input("Введите три целых числа: ").split())
if a > b and a > c:
    m = a
if b > a and b > c:
    m = b
else:
     m = c
print("Максимальное число ", m)