import math
k = 10 + 26 + 8164
a = math.ceil(math.log2(k))
b = 156*1024*8
s = 835
min_len = math.ceil(b / (s*a))
print(min_len)