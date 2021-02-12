string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
lista = string.split(' ')
print(f'lista default {lista}')
resultado = [item.upper() for item in lista]
print(f'list comp. em Upper() {resultado}')
numeros = [x for x in range(21)]
print(f'numeros gerados : {numeros}')
quadrados = [valor ** 2 for valor in numeros]
print(f'quadrado de numeros : {quadrados}')

mod = [numero for numero in numeros if numero % 2 == 0]
print(f'mostra mod 2 = 0 : {mod}')

mods = [numero for numero in quadrados if numero % 2 == 0 if numero % 3 == 0]
print(f'mostra mod 2 = 0 e mod 3 = 0 : {mods}')

r = [str(numero)+':par,' if numero % 2 == 0 else str(numero)+':impar,' for numero in range(10)]
print(r)