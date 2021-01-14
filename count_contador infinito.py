from types import GeneratorType

variavel = ((x,y) for x,y in zip('Alo','Alo'))

print(f'é um gerador? {isinstance(variavel,GeneratorType)}')

'''
count - itertools
'''
from itertools import count

contador = count(start=5,step=1)
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

'''
cuidado para nao fazer isso
'''
for valor in contador:
    print(round(valor,2))
    if valor > 10:
        break

print('x'*80)

contador1 = count()
lista = ['Luiz','Maria', 'Joao']
lista = zip(contador1,lista)
print(list(lista))

