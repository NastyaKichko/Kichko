def f(c,e,step=0):
    if c>e or step>7:
        return 0
    if c == e:
        return step==7
    if c < e :
        return f(c+1,e,step+1) + f(c+4,e,step+1) + f(c*2,e,step+1)

print(f(3,27))
