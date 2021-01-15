import sys
import time

#lista normal
l1 = [x for x in range(100000)]

#gerador
l2 = (x for x in range(100000))

print(f'tamanho  da lista l1 e de: {sys.getsizeof(l1)}\ntamanho do gerador e de: {sys.getsizeof(l2)}')

print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))

for v in l2:
    print(v)


