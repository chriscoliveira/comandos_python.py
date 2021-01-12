# def saudacao(nome, saudacao):
#     print("Ola " + nome + ", " + saudacao + "\n\n")
#
#
# saudacao("Christian", "Beleza?")


# def soma3(numero1, numero2, numero3):
#     soma = int(numero1) + int(numero2) + int(numero3)
#     print("A soma dos numeros: " + str(numero1) + "+" + str(numero2) + "+" + str(numero3) + " = " + str(soma) + "\n\n")
#
#
# numero1 = input("Digite o 1 numero ")
# numero2 = input("Digite o 2 numero ")
# numero3 = input("Digite o 3 numero ")
# soma3(numero1, numero2, numero3)

# def percentual(valor, porcentagem):
#     total = valor+(valor*porcentagem/100)
#     return total
#
# valor = percentual(100,10)
# print(valor)

# def fizzbuzz(numero):
#     if numero % 3 == 0 and numero % 5 ==0:
#         return 'FizzBuzz'
#     elif numero % 3 == 0:
#         return "Fizz"
#     elif numero % 5 == 0:
#         return "Buzz"
#     else:
#         return numero
# print(fizzbuzz(30))

# def funcaoescreve():
#     return 'Ola Christian'
#
# def funcaochama(funcao):
#     return funcao()
#
# resultado = funcaochama(funcaoescreve)
# print(resultado)


def mestre(funcao,*args,**kwargs):
    return funcao(*args,**kwargs)

def oi(nome):
    return f'Oi {nome}'

def saudacao(nome,saudacao):
    return f'{saudacao} {nome}'


executar = mestre(oi,'Christian')
print(executar)
executar2 = mestre(saudacao,'Christian',saudacao='Boa tarde')
print(executar2)