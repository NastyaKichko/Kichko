n = int(input('n='))
aa = 0
if 1<n<27:
    for i in range(100,1000):
        a = i // 10 % 10
        b = i % 10
        c = i // 100
        d = a+b+c
        if d == n:
            aa +=1
    print(aa)
else:
    print('ошибка')
