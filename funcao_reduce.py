from dados import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda acumulador, item: item + acumulador, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos,0)
print(soma_precos)


soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idades)
