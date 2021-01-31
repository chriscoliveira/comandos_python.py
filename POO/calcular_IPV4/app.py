from calc_ipv4 import CalcIPv4
import re

# calc_ipv4 = CalcIPv4(ip='10.18.3.10', mascara='255.255.255.0')
# calc_ipv4 = CalcIPv4(ip='192.168.0.1',prefixo=24)
# calc_ipv4.exibe_info_rede()

while True:
    masc = ''
    cidr = 0
    ip = input('\nDigite um ip IP valido: ')
    masc_ou_cidr = input('O que quer usar? 1-mascara 2-Cidr? ')
    if masc_ou_cidr == '1':
        masc = str(input('Digite a mascara de rede: '))
    elif masc_ou_cidr == '2':
        cidr = int(input('Digite o Cidr da rede: '))
    else:
        pass

    if masc_ou_cidr == '1':
        calc_ipv4 = CalcIPv4(ip=ip, mascara=masc)
        calc_ipv4.exibe_info_rede()
    if masc_ou_cidr == '2':
        calc_ipv4 = CalcIPv4(ip=ip, prefixo=cidr)
        calc_ipv4.exibe_info_rede()
    print('#' * 50 + '\n')

