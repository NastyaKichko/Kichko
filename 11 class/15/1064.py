#(x + 3y ≠ 27) ∨ ((A > x) ∧ (A > y))
def f(x,y):
    return((x + 3*y != 27) or ((A > x) and (A > y)))
for A in range(200):
    if all(f(x,y)==1 for x in range(0,30)for y in range(0,210)):
        print(A)
#28