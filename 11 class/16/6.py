from functools import*
@lru_cache(None)
def F(n):
    if n <= 18:
        return n+3
    if n%3==0 and n > 18:
        return (n//3)*F(n//3) + n-12
    if n%3!=0 and n > 18:
        return F(n-1) + n*n + 5
k=0
for i in range(1,801):
    if all(int(j) % 2==0 for j in str(F(i))):
        k+=1
print(k)