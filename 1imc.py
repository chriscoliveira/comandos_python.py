nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
faixa = 0

imc = peso / (altura ** 2)
if imc < 18.5:
    faixa = 'Magreza'
if imc > 18.5 and imc < 24.9 :
    faixa = 'Normal'
if imc >24.9 and imc < 30 :
    faixa = 'Sobrepeso'
if imc > 30:
    faixa = 'Obesidade'
                
#print('Ola '+nome+', seu IMC e de '+str(imc)+', sua faixa esta em: '+str(faixa))
#print('Ola {0}, seu IMC e de {1}, sua faixa esta em: {2}'.format(nome, imc, faixa))
print(f'Ola {nome}, seu IMC e de {imc:.2f}, sua faixa esta em: {faixa}')
