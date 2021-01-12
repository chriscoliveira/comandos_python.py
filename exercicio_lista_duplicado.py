lista_de_listas_de_inteiros = [
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],

]

for lista_individual in lista_de_listas_de_inteiros:
    print(f'\nLista - {lista_individual}')
    lista_comparar = []
    repetido = set()
    for numero in lista_individual:
        num_atual = []
        num_atual.append(numero)
        lista_comparar.append(numero)
        x = set(num_atual)
        y = set(lista_comparar)
        print(x, y)
        if len(lista_comparar) > 1:
            z = x & y
            print(z)
            break


