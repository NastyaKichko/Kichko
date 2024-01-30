n = 185
c = 0
for i in range(n//15):
    for j in range(n//17):
        for k in range(n//21):
            if (i*15 + j*17 + k*21)>185:
                break
            elif (i*15 + j*17 + k*21)==185:
                c+= 1
print(c)