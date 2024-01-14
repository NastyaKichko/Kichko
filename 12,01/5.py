a, b, c, d, e = map(int, input("Введите пять целых чисел: ").split())
if a > b and a > c and a > d and a > e:
    m = a
elif b > a and b > c and b > d and b > e:
    m = b
elif d > a and d > c and d > b and d > e:
    m = d
elif c > a and c > b and c > d and c > e:
    m = c
else:
     m = e
print("Максимальное число ", m)