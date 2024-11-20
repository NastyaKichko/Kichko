import sys
sys.setrecursionlimit(100)
def g(n):
    if n<10:
        return n
    return g(n - 2) + 1

def f(n):
    return g(n-1)

k=0
for n in range(1,100+1):
    for j in range(1,11):
        if f(n) == j**2:
            k+=1


print(k)