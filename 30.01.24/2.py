a = 10
b = 5
c = 0.5
for i in range(11):
    for j in range(21):
        for k in range(201):
            rub= i*a + j*b + k*c
            head= i + j + k
            if (rub<=100) and head==100:
                print(f'быков {i} коров {j} телят {k}')