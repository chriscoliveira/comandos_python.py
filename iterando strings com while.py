frase = 'Christian de Carvalho Oliveira'
tamanho_frase = len(frase)
print(tamanho_frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    #print(frase[contador], contador)
    if frase[contador].lower() == 'a':
        nova_string += '4'
    elif frase[contador].lower() == 'e':
        nova_string += '3'
    elif frase[contador].lower() == 'i':
        nova_string += '1'
    elif frase[contador].lower() == 'o':
        nova_string += '0'
    else:
        nova_string += frase[contador]
    print(nova_string)
    contador += 1
