lista = [0, 1, 2, 3, 4, 5]
#verifica se a lista e iteravel
print(hasattr(lista, '__iter__'))

#verifica se a lista e um iterador
print(hasattr(lista, '__next__'))

#transfoma a lista em um iterador
lista = iter(lista)
print(hasattr(lista, '__next__'))

x=0
while x < 5:
    print(next(lista))
    x+=1

import sys , time

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r

g = gera()
for v in g:
    print(v)

