a,b = map(int, input('введите границы диапозона:\n').split())
for i in range(a,b+1):
    k = 0
    for j in range(1,i):
        if i % j==0:
            k+=1
        if k > 1:
            break
    if k == 1:
        print(i)