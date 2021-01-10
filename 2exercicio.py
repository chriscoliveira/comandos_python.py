import datetime

nome = 'Christian'
idade = 36
ano = datetime.date.today().year
ano_nascimento = ano - idade
peso = 84.5
altura = 1.72
imc = peso / (altura ** 2)
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.\nO IMC de {nome} é {imc:.02f}.\n{nome} nasceu em {ano_nascimento}')