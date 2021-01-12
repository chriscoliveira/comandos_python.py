from random import randint

'''
validar o cpf
'''
CPF = input("Digite o numero do seu CPF: ")
conferencia = CPF[:-2]
contadorr = 10
digito = 0
passo = 0
soma = 0
tamanho = len(conferencia)

# calcula o primeiro digito verificador
while contadorr > 1:
    # print(str(conferencia[passo]) + "x" + str(contadorr) + "=")
    soma += int(conferencia[passo]) * contadorr
    contadorr -= 1
    passo += 1
digito = 11 - (soma % 11)
if digito > 9:
    digito = 0

conferencia += str(digito)
contadorr = 11
passo = 0
soma = 0

while contadorr > 1:
    # print(str(conferencia[passo]) + "x" + str(contadorr) + "=")
    soma += int(conferencia[passo]) * contadorr
    contadorr -= 1
    passo += 1
digito = 11 - (soma % 11)
if digito > 9:
    digito = 0

conferencia += str(digito)
contadorr = 11

if int(CPF) == int(conferencia):
    print("CPF " + CPF + " eh valido")
else:
    print("CPF " + CPF + " eh invalido")

####################################################### FIM DO VALIDADOR


####################################################### gerador de CPF
conferencia = str(randint(100000000, 999999999))
contadorr = 10
digito = 0
passo = 0
soma = 0
tamanho = len(conferencia)

# calcula o primeiro digito verificador
while contadorr > 1:
    # print(str(conferencia[passo]) + "x" + str(contadorr) + "=")
    soma += int(conferencia[passo]) * contadorr
    contadorr -= 1
    passo += 1
digito = 11 - (soma % 11)
if digito > 9:
    digito = 0

conferencia += str(digito)
contadorr = 11
passo = 0
soma = 0

while contadorr > 1:
    # print(str(conferencia[passo]) + "x" + str(contadorr) + "=")
    soma += int(conferencia[passo]) * contadorr
    contadorr -= 1
    passo += 1
digito = 11 - (soma % 11)
if digito > 9:
    digito = 0

conferencia += str(digito)
contadorr = 11
print(conferencia)