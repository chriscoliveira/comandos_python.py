# primeiro
numero = input('Digite um numero: ')
try:
    if int(numero) % 2 == 0:
        print('O numero digitado e par')
    else:
        print('O numero digitado e impar')
except:
    print('o valor informado nao e um numero inteiro')

# segundo
hora = int(input('Digite que horas sao agora Ex. 18: '))
try:
    if 0 < hora < 12:
        print('Bom dia')
    elif hora > 11 and hora < 18:
        print('Boa tarde')
    if hora > 18 and hora < 24:
        print('Boa noite')
except:
    print('O valor informado não é uma hora valida')

#terceiro
nome = input('Digite seu nome: ')
try:
    if len(nome) < 5:
        print('Seu nome e pequeno')
    elif 5 < len(nome) < 6:
        print('seu nome e normal')
    elif len(nome) > 6:
        print('seu nome e grande')
except:
    print('Isso nao é um nome valido')