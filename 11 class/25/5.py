def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x % i==0:
            d.add(i)
            d.add(x//1)
    return sorted(d)
a=250200 +1
for i in range(a,a+2000):
    D = div(i)
    s = max(D) + min(D) if len(D)>0 else 0
    if s != 0 and s% 123 ==17:
        print(i,s)