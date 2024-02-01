n = int(input("Введите n: "))
r = []
for i in range(1, n+1):
    a = [int(d) for d in str(i)]
    if all(d != 0 and i % d == 0 for d in a):
        r.append(i)
print(r)