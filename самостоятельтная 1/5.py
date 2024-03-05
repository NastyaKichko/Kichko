def f(n):
    if n == 0:
        return 1
    if n>0 and n%2==0:
        return f(n // 100) * (n % 10)
    if n>0 and n%2==0:
        return f(n // 100)

k=0
for i in range (10**2,6*(10**3)+1):
    if f(i)==2:
        k+=1
print(k)
