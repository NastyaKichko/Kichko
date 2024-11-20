def line(s, t):
    k, b = map(float, s.split('x'))
    print(f'k = {k:<5} b = {b:<5}')
    x,y = map(float, t.split(';'))
    print(f'x = {x:<5} y = {y:<5}')
    if y==k*x+b:
        print(True)
    else:
        print(False)
line("1x+6", "1;7")



