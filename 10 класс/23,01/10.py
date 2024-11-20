b = int(input('Введите кол-во мальчиков: '))
g = int(input('Введите кол-во девочек: '))
a = ''
if (b > 2 * g) or (g > 2 * b):
    print('Нет решения.')
elif b >= g:
    k = b - g
    for bgb in range(k):
        a += 'BGB'
    for bg in range(g - k):
        a += 'BG'
else:
    k = g - b
    for gbg in range(k):
        a += 'GBG'
    for gb in range(b - k):
        a += 'GB'
print('ответ: ',a)