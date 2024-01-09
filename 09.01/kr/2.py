import math

x1,y1 = [float(i) for i in input("Введите координаты точки A: ").split()]
x2,y2 = [float(i) for i in input("Введите координаты точки B: ").split()]
d = math.sqrt((y2-y1)**2+(x2-x1)**2)
print("Длина отрезка AB = ", d)
