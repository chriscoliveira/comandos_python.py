#gerar 2 contadores um progressivo e outro regressivo e exibir a contagem lado a lado

numero = 10
contadorP, contadorR = 0, numero

while contadorP < numero:
    print(contadorP, contadorR)
    contadorP += 1
    contadorR -= 1
