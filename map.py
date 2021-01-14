from dados import produtos, pessoas, lista

print(lista)
nova_lista = map(lambda x: x*2, lista)
print(list(nova_lista))

#list comprehension
nova_lista1 = [z *2 for z in lista]
print(nova_lista1)

#aumento de 5%nos produtos
def aumento(p):
    p['preco'] = round(p['preco'] * 1.05,2)
    return p

novos_produtos = map(aumento, produtos)
for produto in novos_produtos:
    print(produto)

def aumento_idade(p):
    p['nova_idade'] =round(p['idade'] *1.20)
    return p

#nomes = map(lambda p: p['nome'],pessoas)
nomes = map(aumento_idade,pessoas)

for pessoa in nomes :
    print(pessoa)

