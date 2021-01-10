"""
repeticao while
"""
#loop infinito
"""
while True:
    nome = input("Qual o seu Nome? ")
    print(f'Ola {nome}')
"""
"""
x = 0
while "x < 50:
    x += 1
    if x % 2 == 1:
        continue
    if x == 10:
        break
    print(x)

x = 0
while x < 5:
    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1
"""

contador = 1
acumulador = 1

while contador <10:
    print(contador, acumulador)

    if contador > 10:
        print("break")
        break

    acumulador = acumulador + contador
    contador +=1
print("fim")

