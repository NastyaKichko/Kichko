n = int(input("введите натуральное число:\n"))
dig = ' '
while n>0:
    t_dig = n%10
    n//=10
    if dig == t_dig:
        print('да')
        break
    dig = t_dig
else:
    print('нет')