texto = 'valor'
lista = [1, 2, 3, 4, 'oi', 4.3, True]
print(lista)
print(lista[0:3])
print(lista[:3])
print(lista[3:])
print(lista[::2])
print(lista[::-1])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

l1.extend(l2)
l1.extend('a')
print(l1)

l2.append('b')
l2.insert(0, 'banana')
print(l2)

l2.pop()
print(l2)

l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l4)
del (l4[3:5])
print(l4)
print(max(l4), min(l4))

l5 = list(range(1, 100, 8))
print(l5)
soma = 0
for valor in l5:
    soma += valor
    print(soma)

for elemento in lista:
    print(f'O tipo do elemento {elemento} é {type(elemento)}')


#######################################################
secreto = 'perfume'
digitado = []
acerto = []
chances = 3
while True:
    if chances == 0:
        print('Voce perdeu')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas 1 letra')
        continue
    digitado.append(letra)

    if letra in secreto:
        print(f'Acertou {len(digitado)} letra: {letra}\n')
    else:
        print(f'A letra {letra} nao existe!')
        chances -= 1
        print(f'Voce ainda tem {chances} tentativas')
        digitado.pop()

    secreto_tmp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitado:
            secreto_tmp += letra_secreta
        else:
            secreto_tmp += '*'

    if secreto == secreto_tmp:
        print('Voce ganhou!')
        break
    print(secreto_tmp)
