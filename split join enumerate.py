string = 'O Brasil e o pais do futebol, o Brasil e penta'
lista = string.split(' ')
print(lista)
print("##########################\n")

lista2 = string.split(',')
print(lista2)
print("##########################\n")

palavra = ''
contagem = 0

for valor in lista:
    print(f'A palavra {valor} apareceu {lista.count(valor)}x na frase')
    qtde_vezes = lista.count(valor)
    if qtde_vezes > contagem:
        contagem = qtde_vezes
        palavra = valor

print(f'a palavra que apareceu mais vezes e "{palavra}" {contagem}x')
print("##########################\n")

for valor in lista2:
    print(valor.strip().capitalize())
print("##########################\n")

lista3 = lista
print(lista3)
lista4 = '_'.join(lista3)
print(lista4)
print("##########################\n")

for indice, valor in enumerate(lista):
    print(indice, valor)
print("##########################\n")

lista5 = [
    'Luiz',
    'Joao',
    'Maria',
]
for indice, nome in enumerate(lista5):
    print(indice, nome)