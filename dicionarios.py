d1 = {'chave1': 'valor da chave'}
print(d1)

d1['novachave'] = 'valor da nova chave'
print(d1)
print(d1['chave1'])


d2 = dict(chave1='Valor da chave 1', chave2='Valor da chave 2')
print(d2)

d3 = {
    'str': 'String',
    123: 'Inteiro',
    (1,2,3,4,5): 'Tupla'
}
print(d3[(1,2,3,4,5)])

if 'str' in d3:
    print(d3['str'])

print(d3.get(123))

if d3.get('str') is not None:
    print(d3.get('str'))
print('qqqqqqqqqqqqqqqqqqqqqqqqqq')
d3.update({'nova_chave':'novovalor'})

print(d3)

del d3['nova_chave']
print((d3))

print('str' in d3)
print('str' in d3.keys())
print('String' in d3.values())
print(len(d3))

print('\n\n\n\niterando...\n')
for k in d3:
    print(k)
print('\n')
for v in d3.values():
    print(v)
print('\n')
for i in d3.items():
    print(i[0],i[1])
print('\n')
for k, v in d3.items():
    print(k, v)


clientes = {
    'cliente1':{
        'nome':'Christian',
        'sobrenome':'Carvalho'
    },
    'cliente2':{
        'nome':'Patricia',
        'sobrenome':'Carvalho'
    },
    'cliente3':{
        'nome':'Joana',
        'sobrenome':'Lucia'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k , dados_v in clientes_v.items():
        print(f'\t{dados_k}={dados_v}')

####nao fazer isso
d4 = {1:'a',2:'b',3:'c'}
# v = d4
# print(v)
# print(d4)
# v[1] = 'Luiz'
# print(v)
# print(d4)
####fazer assim
v = d4.copy()
print(v)
print(d4)
v[1] = 'Luiz'
print(v)
print(d4)
