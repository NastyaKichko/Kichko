n=int(input())
s=''
a = 0
for i in range(1,n+1):
    s+=str(i)
    a+=1
    if len(s)==n:
        break
print(a)