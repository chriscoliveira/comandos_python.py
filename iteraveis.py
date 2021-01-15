#lists, tuples, str -> sequences = iteravel
nome='Christian'
gerador = (letra for letra in nome)
# for letra in nome:
#     print(letra)
#
# print('#' * 80)
#
# for letra in nome:
#     print(letra)
#
# print(nome)

#
# iterador = iter(nome)
#
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print('#'*80)
# for v in iterador:
#     print(v)

print('#'*80)
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

