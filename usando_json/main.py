from usando_json.dados import *
import json

# lendo apartir de outra classe 
dados_json = json.dumps(clientes_dicionario, indent=4)
print(dados_json)

# convertendo para dicionario
dicionario = json.loads(clientes_json)
for chave, valor in dicionario.items():
    print(chave, valor)

# salvar dicionar em json
with open('clientes.json', 'w')as arquivo:
    json.dump(clientes_dicionario, arquivo,indent=4)

# ler json para dicionario
with open('clientes.json', 'r')as arquivo:
    dados = json.load(arquivo)
for chave,valor in dados.items():
    print(chave)
    print(valor)