def R(N):
    bn = f'{N:b}'
    if bn.count('1')%2==0:
        bn = '10'+ bn[2:] + '0'
    else:
        bn = '11'+bn[2:]+'1'
    return int(bn,2)
for N in range(4,50):
    if R(N)>50:
        print(N)
        break