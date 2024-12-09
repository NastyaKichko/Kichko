from functools import*
@lru_cache(None)
def F(n):
    if n <= 15:
        return n*n + 11
    if n%2==0 and n > 15:
        return F(n//2) + n*n*n - 5*n
    if n%2!=0 and n > 15:
        return F(n-1) + 2*n + 3
k=0
for n in range(1,1000):
    if str(F(n)).count('6')>=3:
        k+=1
print(k)