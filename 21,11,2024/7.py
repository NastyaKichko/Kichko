from ipaddress import*
ip_u1 = '157.127.182.76'
ip_u2 = '157.127.190.80'
for mask in range(33):
    net1 = ip_network(f'{ip_u1}/{mask}',0)
    net2 = ip_network(f'{ip_u2}/{mask}', 0)
    if net1 != net2:
        print(mask)