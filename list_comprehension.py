l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]
print(ex1)
print()

ex2 = [v *2 for v in l1]
print(f'{ex2}\n')

ex3 = [(v,v2) for v in l1  for v2 in range(3)]
print(f'{ex3}\n')

l2 = ['Luiz','Mauro', 'Maria']

ex4 = [v.replace('a','@').upper() for v in l2]
print(f'{ex4}\n')

tupla = (
    ('chave','valor'),
    ('chave2', 'valor2'),
)

ex5 = [(x,y) for y,x in tupla]
print(f'{ex5}\n')
ex5 = dict(ex5)
print(f'{ex5}\n')


l3 = list(range(40))
print(f'{l3}\n')

ex6 = [v for v in l3 if v % 2 ==0]
print(f'{ex6}\n')


ex7 = [v for v in l3 if v % 2 ==0 if v % 8 ==0]
print(f'{ex7}\n')

ex8 = [v if v % 3 ==0 and v % 8 ==0 else ' ' for v in l3]
print(f'{ex8}\n')
