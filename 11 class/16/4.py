from functools import*
@lru_cache(None)
def F(n):
    if n > 25:
        return 2*n*n*n + 1
    if n <= 25:
        return F(n+2) + 2*F(n+3)
k=0
for n in range(1,1000):
    if F(n)%11==0:
        k+=1
print(k)
