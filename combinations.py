from itertools import combinations, permutations,product

pessoas = ['Christian','Patricia','Joana','Rosa', 'Luiz']

print('#Combbinacao'*6)
for grupo in combinations(pessoas,4):
    print(grupo)

print('#Permutacao'*6)

for grupo in permutations(pessoas,2):
    print(grupo)

print('#Produto'*6)

for grupo in product(pessoas,repeat=3):
    print(grupo)


