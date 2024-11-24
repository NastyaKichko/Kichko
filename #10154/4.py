from ipaddress import*
ip_u ='148.195.140.28'
ip_s = '148.195.140.0'
for mask in range(33):
    net = ip_network(f'{ip_u}/{mask}',0)
    if ip_s in str(net):
        print(bin(int(net.netmask)))
#ответ: 22