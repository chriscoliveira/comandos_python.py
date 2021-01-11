string = '0123456789012345678901234567890123456789012345678901234567890123456789'
contador = 10
contadores = [(s, s+contador) for s in range(0,len(string),contador) ]
lista_separada = [string[s:s+contador] for s in range(0,len(string),contador)]
listajunta = '.'.join(lista_separada)

print(f'{string}\n{lista_separada}\n{listajunta}')
print(contadores)