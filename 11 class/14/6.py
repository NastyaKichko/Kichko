for x in '0123456789ABCDEFGHI':
    a = f'55{x}36'
    b = f'{x}2724'
    s = int(a,19) + int(b,19)
    if s % 11 == 0:
        print(s//11)
        #135122