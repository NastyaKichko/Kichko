n = int(input("Введите n: "))
for i in range(1, n+1):
    i2=i
    while i2>0:
        dig=i2%10
        i2//=10
        if dig==0 or i%dig!=0:
            break
    else:
        print(i,end=' ')