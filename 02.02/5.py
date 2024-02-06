def squared(a, b, k):
    n = 1
    for x in range (a, b+1):
        if (x*x % k != 0):
            print(f"{x*x:<4}", end=' ')
        n+=1
        if n>10:
            n=1
            print()
squared(4, 33, 9)
