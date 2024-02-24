def tr(a,b,c):
    if a + b <= c and a + c <= b and c + b <= a:
        return False
    if a**2 == b**2 + c**2 or c**2 == b**2 + a**2 or b**2 == a**2 + c**2:
        return True
    return False
a,b,c=map(float,input('введите стороны :\n').split())
if tr(a,b,c):
    print('треугольник существует, прямоугольный')
else:
    print('треугольник не существует или не прямоугольный')


