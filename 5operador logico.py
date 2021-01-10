'''
and, or, not
in e not in
'''
idade = 22
vazio = 0
idade_menor = 20
idade_maior = 30
nome = 'Christian'

#and
if idade > idade_menor and idade < idade_maior:
    print('idade ideal')

#or
if idade > idade_menor or idade < idade_maior:
    print('atende no minimo 1 dos requisitos')

#not
if not idade > idade_menor:
    print('idade abaixo do pedido')

if not vazio:
    print('valor vazio ou falso na variavel')

#in
if 'h' in nome:
    print('Letra h existe no nome')
#not in
if 'z' not in nome:
    print('Letra z nao existe no nome')

