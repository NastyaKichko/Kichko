n = int(input("введите натуральное число:"))
sum = 0
while n % 10 != 0:
    sum = sum + n%10
    n = int(n/10)
print('сумма цифр ', sum)