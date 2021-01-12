s1 = {1,2,3,4,5,6}
print(type(s1),s1)

for v in s1:
    print(v)

s2 = set()
s2.add(1)
s2.add(100)
print(s2)
s2.discard(1)
print(s2)

s2.update('Python')
print(s2)

s2.update([1,2,3,4,5],{1,2,36,7,8,9})
print(s2)

S1 = {0,1,2,3,4,5}
S2 = {1,2,3,4,5,6}
print(f'\n\nConjunto S1 {S1}\nConjunto S2 {S2}\n')
#uniao dos conjuntos
S3 = S1 | S2
print(f'Uniao dos conjuntos {S3}')

#interseccao
S3 = S1 & S2
print(f'Interseccao dos conjuntos {S3}')

#diferenca
S3 = S1 - S2
print(f'Diferenca dos conjuntos S1 - S2 {S3}')

#diferenca simetrica
S3 = S1 ^ S2
print(f'Diferenca simetrica dos conjuntos  {S3}')

