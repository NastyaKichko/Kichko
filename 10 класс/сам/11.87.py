from random import randint

n = 22
A = [randint(-170,170) for _ in range(n)]
print(f'массив:\n{" ".join(str(i) for i in A)}')
b=[]
c=[]
for i in range(n):
    if A[i]>= 0:
        b.append(A[i])
    else:
        c.append(A[i])
k = sum(i for i in b)
l= sum(i for i in c)
print(f'girls: {k/len(b)}')
print(f'boys: {l/len(c)}')