#(2x + 3y ≠ 72) ∨ ((A > x) ∧ (A > y))
def f(x,y):
    return((2*x + 3*y != 72) or ((A > x) and (A > y)))
for A in range(100):
    if all(f(x,y)==1 for x in range(0,80)for y in range(0,110)):
        print(A)
#37