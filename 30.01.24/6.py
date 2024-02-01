n = int(input('Введите n:'))
m = int(input('Введите m:'))
for i in range(n):
    s = 0
    j = i
    while j>0:
        s+=(j%10)**2
        j=j//10
    if s==m:
        print(i)