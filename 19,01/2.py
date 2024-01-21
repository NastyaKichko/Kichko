a, b = map(int,input().split())
r, s = 0, 1
if b < 0:
    b =-b
    s = -1
while b:
    r = r + a
    b = b - 1
if s < 0:
    r = - r
    print(r)
