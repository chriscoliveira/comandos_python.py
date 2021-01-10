texto = 'Python'
"""
for letra in texto:
    print(letra)
"""

for numero in range(10):
    print(numero)

for numero in range(10,0,-1):
    print(numero)

for numero in range(0,10,2):
    print(numero)

print('###########')

nova = ''
for letra in texto:
    if letra == 't':
        nova += letra.upper()
    elif letra == 'h':
        continue
        nova += letra.upper()
    else:
        nova += letra
print(nova)