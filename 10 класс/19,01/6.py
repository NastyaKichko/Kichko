n = int(input("введите натуральное число:\n"))
dig = []
while n:
    s = n%10
    if s in dig:
        print('да')
        break
    else:
        dig.append(s)
    n//=10
else:
    print('нет')