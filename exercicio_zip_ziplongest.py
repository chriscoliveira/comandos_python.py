from itertools import zip_longest, count

lista_a = [10, 20, 30, 40, 50, 60, 70]
lista_b = [1, 2, 3, 4]

# lista_soma = []
# indice = count()
# cont = len(lista_a)
#
# if len(lista_b) > cont:
#     cont = len(lista_b)
#
# lista_ab = zip_longest(indice, lista_a, lista_b)
# for i, a, b in lista_ab:
#     if i > cont - 1:
#         break
#     else:
#         if a == None:
#             a = 0
#         if b == None:
#             b = 0
#         lista_soma.append(float(a) + float(b))
# print(list(lista_soma))


# lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
# print(lista_soma)

# melhor forma de usar
# usando list comprehension
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)
