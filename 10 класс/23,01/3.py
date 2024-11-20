a=int(input('N: '))
for i in range(1,a):
    b = 10
    while i>=b:
        b = b*10
    if ((i*i%b)==i):
        print(f'{i}*{i}=',i*i)