s = int(input('Введите s:'))
for i in range(1,s+1):
    if s % i == 0:
        j = s//i
        print(i,j)