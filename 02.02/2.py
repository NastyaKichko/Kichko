def dig1(n):
    c = []
    if n < 0:
        n = -n
    while n > 0:
        b = n % 10
        c.append(b)
        n = n // 10
    c.reverse()
    for b in c:
        print(b)
n = int(input('введите натуральное число: '))
dig1(n)