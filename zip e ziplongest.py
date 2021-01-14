from itertools import zip_longest,count

cidades = ['Sao Paulo','Belo Horizonte','Salvador','Monte Belo','Jacarei','Sao Jose']
estados = ['SP','MG','BA']

cidades_estados = zip(estados,cidades)

# for valor in cidades_estados:
#     print(valor)

print(cidades_estados)
print(list(cidades_estados))

print('#'*20)

cidades_estados1 = zip_longest(estados,cidades,fillvalue='Sem Estado')
print(list(cidades_estados1))

print('#'*20)

indice = count()

cidades_estados2 = zip_longest(indice,estados,cidades,fillvalue='Sem dados')

for i,e,c in cidades_estados2:
    print(i,e,c)
