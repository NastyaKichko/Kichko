a, b = map(int,input().split())
i = a
while i <= b:
    print('{0}*{0}={1}'.format(i,i**2))
    i+=1