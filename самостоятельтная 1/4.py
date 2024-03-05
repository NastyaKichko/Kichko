'''
import sys
sys.setrecursionlimit(2**30)
'''
def f(n):
    if n < 2:
        return n
    return f(n // 2) + f(n % 2)

k=0
for i in range (1,2**10+1):
    print(f'для {i}={f(i)}')
#    if f(i)==27:
#        k+=1
#print(k)