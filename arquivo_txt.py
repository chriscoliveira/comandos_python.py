
# try:
#     file = open('arquivo.txt','w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()

'''
r = modo leitura
w = modo escrita
w+ = modo escrita porem apaga tudo no arquivo
a = modo append
'''

with open('arquivo.txt','w+') as file:
    file.write('Linha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')
    file.write('Linha4\n')

    file.seek(0)
    print(file.read())

import json
d1 = {
    'Pessoa 1': {
        'nome':'Christian',
        'idade':36
    },
    'Pessoa 2': {
        'nome':'Patricia',
        'idade':40,
    }
}
d1_json = json.dumps(d1,indent=True)
print(d1)
print(d1_json)
with open('arquivo.json','w+') as file:
    file.write(d1_json)