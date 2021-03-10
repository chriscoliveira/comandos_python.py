valor = '50 centavos real asa '
num = valor.split()
resto = str(num[1:]).replace("'",'').replace(',','').replace('[','').replace(']', '')
print(num[0])
print(resto,type(resto))