from ipaddress import*
ip_s = '111.81.192.0'
ip_u = '111.81.208.27'
for mask in range(33):
    net = ip_network(f'{ip_u}/{mask}',0)
    if ip_s in str(net):
        print(net.netmask)