def f(n):
    x=0
    while n>0:
        a = n % 10
        n = n // 10
        x+=a
    return x
print(f(123))