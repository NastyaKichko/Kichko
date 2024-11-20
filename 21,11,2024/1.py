from ipaddress import*
mask = '255.255.248.0'
ip_s = '135.12.171.214'
net = ip_network(f'{ip_s}/{mask}',0)
print(net)
