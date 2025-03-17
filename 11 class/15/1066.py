#(y + 4x ≠ 120) ∨ (x > A) ∨ (y > A)
def f(x,y):
    return((y + 4*x != 120) or (x > A) or (y > A))
for A in range(200):
    if all(f(x,y)==1 for x in range(0,130)for y in range(0,210)):
        print(A)
#23