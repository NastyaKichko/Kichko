import math

a = int(input("ст 1: "))
b = int(input("ст 2: "))
c = int(input("ст 3: "))
p = (a + b + c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print (s)