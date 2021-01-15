from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

nova_lista1 = [x for x in lista if x > 5]
print(list(nova_lista1))

print('x'*80)


lista_produtos = filter(lambda  p: p['preco'] > 50, produtos)
for produto in lista_produtos:
    print(produto)


print('x'*80)

def filtra(prod):
    if prod['preco'] > 50:
        prod['maior que 50'] = True
    return True

lista_produtos1 = filter(filtra,produtos)

for prod in lista_produtos1:
    print(prod)



print('x'*10)

def filtraidade(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

lista_maior = filter(filtraidade,pessoas)
for pessoa in lista_maior:
    print(pessoa)

print('x'*10)

lista_menor = filter(lambda i: i['idade'] < 18, pessoas)
for idade in lista_menor:
    print(idade)

print('x'*10)
