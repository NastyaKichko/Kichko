from ipaddress import*
ip_s = ip_address('115.198.0.0')
mask = '255.254.0.0'
net = ip_network(f'{ip_s}/{mask}')
k = 0
for ip in net:
    s = '.'.join(f'{int(x):>08b}' for x in str(ip).split('.'))
    if s.count('1')% 5 == 0:
        k+=1
print(k)