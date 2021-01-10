"""
:s  strings
:d  inteiros
:f  float
>   esquerda
<   direita
^   centro
"""
valor = 3.3456789
print('{:.2f}'.format(valor))
valor1 = 15
print(f'valor formatado de {valor1:0<5f}')
print(f'valor formatado de {valor1:0>5f}')
print(f'valor formatado de {valor1:0^5}')

nome = 'Christian'
print(f'{nome:$^15}')  # COMPLETA O TAMANHO DA STRING COM $ ATÉ CHEGAR A 15 CARACTERES

eu = 'Christian Carvalho Oliveira'
eu = eu.rjust(50,'#')
print(eu.upper())