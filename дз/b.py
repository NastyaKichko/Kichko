import math

x1 = float(input("координаты точки a(x1): "))
y1 = float(input("координаты точки a(y1): "))
x2 = float(input("координаты точки b(x2): "))
y2 = float(input("координаты точки b(y2): "))
x3 = float(input("координаты точки c(x3): "))
y3 = float(input("координаты точки a(y3): "))
d1 = math.sqrt((y2-y1)**2 + (x2-x1)**2)
d2 = math.sqrt((y3-y2)**2 + (x3-x2)**2)
d3 = math.sqrt((y3-y1)**2 + (x3-x1)**2)
print(f"ab= ",d1)
print(f"bc= ",d2)
print(f"ac= ",d3)