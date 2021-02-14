import random
import string

inteiro = random.randint(10, 20)
print(f'numero aleatorio inteiro {inteiro}')

inteiro2 = random.randrange(900, 1000, 10)
print(f'numero aleatorio inteiro com a func range {inteiro2}')

flutuante = random.uniform(10, 20)
print(f'numero aleatorio float {flutuante}')

flutuante2 = random.random()
print(f'numero aleatorio float usando random {flutuante2}')

lista = ['christian', 'patricia', 'joana', 'rosa', 'luiz', 'adriana']
print(f'lista {lista}')
sorteio = random.choice(lista)
print(f'sorteio da lista {sorteio}')

sorteios = random.choices(lista, k=2)
print(f'2 sorteados {sorteios}, podendo ser repetidos os valores')

sorteios1 = random.sample(lista, 2)
print(f'2 sorteados {sorteios1}, sem repetir os valores')

random.shuffle(lista)
print(f'Embaralha a lista {lista}')


letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%¨&*_-.'
geral = letras + digitos + caracteres
senha = ''.join(random.choices(geral, k=20))
print(f'Senha aleatoria {senha}')
