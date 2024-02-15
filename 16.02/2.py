def tr(a,b,c):
    if (a+b>c and a+c>b and c+b>a) and ((a=(b+c)**0,5) or (c=(b+a)**0,5) or (b=(a+c)**0,5)):
        return True
    return False
a,b,c=map(float,input(':\n').split())
if tr

