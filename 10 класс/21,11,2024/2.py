from ipaddress import*
ip_s = '220.128.96.0'
ip_u = '220.128.112.142'
for mask in range(33):
    net = ip_network(f'{ip_u}/{mask}',0)
    if ip_s in str(net):
        print(net.netmask)
