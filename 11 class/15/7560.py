#(х + у ≤ 30) ∨ (у ≤ х+2) ∨ (у ≥ А)
def f(x,y):
    return((x + y <= 30) or (y <= x+2) or (y >=A))
for A in range(100):
    if all(f(x,y)==1 for x in range(0,40)for y in range(0,110)):
        print(A)
#17