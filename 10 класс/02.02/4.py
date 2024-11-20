def equation(xy1, xy2):
    x1, y1 = map(float, xy1.split(';'))
    x2, y2 = map(float, xy2.split(';'))
    a = (y1-y2)/(x1-x2)
    b = y2 - a * x2
    print(a,b)
equation('0;0', '1;1')