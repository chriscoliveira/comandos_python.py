"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
import re


def prepara_cnpj(cnpj):
    return re.sub(r'[^0-9]','',cnpj) 
 

def dig(cnpj):
    cnpj = cnpj[:-2]
    contador, step, soma, maximo, digito1, digito2,stop= 0, 5, 0,12, 0, 0, 0
    while contador < maximo:
        if step > 1:
            soma = soma + step * int(cnpj[contador])
            #print(f'{cnpj[contador]}x{step}={int(cnpj[contador])*step} = {soma}')
            contador += 1
            step -=1    
        else:
            step = 9
        if contador == maximo: 
            if stop == 0:
                print('---')
                contador = 0
                step = 6
                maximo = 13
                stop = 1
                digito1 = 11-soma%11
                if digito1 > 9:
                    digito1 =0
                soma = 0
                cnpj = cnpj+str(digito1)
            else:
                digito2 = 11-soma%11
                if digito2 > 9:
                    digito2 =0
                cnpj = cnpj+str(digito2)
        

    return cnpj


def verifica_cnpj(cnpj):   
        cnpj_recebido = prepara_cnpj(cnpj)
        if not len(cnpj_recebido) <14: 
            cnpj_validado = dig(cnpj_recebido)
            if cnpj_recebido == cnpj_validado:    
                print(f'O CNPJ {cnpj_recebido} e valido!')
            else:
                print(f'O CNPJ {cnpj_recebido} e invalido!')
        else:
            print('CNPJ Invalido')
    
