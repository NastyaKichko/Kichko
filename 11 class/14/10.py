for x in range(400,10000):
    a = 16**560+16**120-x
    num_16=0
    while a!= 0:
        if a%16==0:
            num_16+=1
         a=a//16
    if num_16==442:
        if num_16<100000:
            num_16=100000
            print(x)
