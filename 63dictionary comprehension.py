lista = [
    ('chave','valor'),
    ('chave2','valor2'),
]

d1 = {x: y*2 for x,y in lista}
print(d1)

d1 = {x: y.upper() for x,y in lista}
print(d1)

d2 = {x:y for x,y in enumerate(range(5))}
print(d2)

d3 = {f'chave_{x}':x**2 for x in range(5)}
print(d3,type(d3))