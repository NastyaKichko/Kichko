def f(x,y):
    return((x < A) or (y < A) or (x + 2*y > 50))
for A in range(200):
    if all(f(x,y)==1 for x in range(0,60)for y in range(0,210)):
        print(A)
    #17